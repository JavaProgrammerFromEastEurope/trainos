from trainos.ecs.component import SpatialComponent


class SpatialSystem:

    def update(self, entity_manager, telemetry):
        spatials = entity_manager.get_components(SpatialComponent)
        for entity_id, spatial in spatials.items():
            telemetry.metric(
              f"entity.{entity_id}.sector",
              spatial.sector_id)
