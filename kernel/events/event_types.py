# kernel/events/event_types.py

class EventTypes:

    SYSTEM_BOOT 		= "system.boot"
    SYSTEM_SHUTDOWN = "system.shutdown"
    TASK_CREATED 		= "task.created"
    TASK_COMPLETED 	= "task.completed"
    TASK_FAILED 		= "task.failed"
    ENTITY_MOVED 		= "entity.moved"
    ENTITY_BLOCKED 	= "entity.blocked"
    SENSOR_UPDATE 	= "sensor.update"
    ALERT_TRIGGERED = "alert.triggered"
