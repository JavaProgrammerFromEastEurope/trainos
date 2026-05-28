from trainos.ecs.component import SpatialComponent


class SpatialSystem:

    def update(self, entity_manager, telemetry):

        spatials = entity_manager.get_components(SpatialComponent)

        for entity_id, spatial in spatials.items():

            # --------------------------------------------------
            # BASIC POSITION DEBUG
            # --------------------------------------------------
            telemetry.metric(
                f"entity.{entity_id}.sector",
                spatial.sector_id,
            )

            telemetry.metric(
                f"entity.{entity_id}.wagon",
                spatial.wagon_id,
            )

            telemetry.metric(
                f"entity.{entity_id}.cell_x",
                spatial.cell_x,
            )

            telemetry.metric(
                f"entity.{entity_id}.cell_y",
                spatial.cell_y,
            )

            # --------------------------------------------------
            # COMBINED KEY (useful for debugging collisions)
            # --------------------------------------------------
            telemetry.metric(
                f"entity.{entity_id}.grid_key",
                f"{spatial.wagon_id}:{spatial.sector_id}:{spatial.cell_x},{spatial.cell_y}",
            )
