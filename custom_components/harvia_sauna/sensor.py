from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE
from .constants import DOMAIN, STORAGE_KEY, STORAGE_VERSION, REGION,_LOGGER

class HarviaHumiditySensor(SensorEntity):
    """Representatie van een vochtigheidssensor."""

    def __init__(self, device, name, sauna):
        """Initialiseer de humidity sensor."""
        self._name = name + ' Humidity'
        self._state = None
        self._device = device
        self._device_id = device.id + '_humidity_sensor'
        self._sauna = sauna
        self._attr_unique_id = device.id + '_humidity_sensor'
        self._attr_icon = 'mdi:water-percent'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return de eenheid die wordt gebruikt."""
        return PERCENTAGE

    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        self._device.humiditySensor = self
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()

class HarviaWifiSensor(SensorEntity):
    """Representatie van de Wifi signaalsterkte."""

    def __init__(self, device, name, sauna):
        """Initialiseer de wifi sensor."""
        self._name = name + ' Wifi Signal'
        self._state = None
        self._device = device
        self._device_id = device.id + '_wifi_sensor'
        self._sauna = sauna
        self._attr_unique_id = device.id + '_wifi_sensor'
        self._attr_icon = 'mdi:wifi'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return de eenheid die wordt gebruikt."""
        return 'dBm'

    @property
    def device_class(self):
        return "signal_strength"

    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        self._device.wifiSensor = self
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()

class HarviaRemainingTimeSensor(SensorEntity):
    """Representatie van de resterende tijd."""

    def __init__(self, device, name, sauna):
        """Initialiseer de sensor."""
        self._name = name + ' Remaining Time'
        self._state = None
        self._device = device
        self._device_id = device.id + '_remaining_time'
        self._sauna = sauna
        self._attr_unique_id = device.id + '_remaining_time'
        self._attr_icon = 'mdi:timer-outline'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        if self._state is None:
            return None
        minutes = int(self._state)
        return f"{minutes // 60:02}:{minutes % 60:02}"

    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        self._device.remainingTimeSensor = self
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()

class HarviaMaxOnTimeSensor(SensorEntity):
    """Representatie van de maximale aan-tijd."""

    def __init__(self, device, name, sauna):
        """Initialiseer de sensor."""
        self._name = name + ' Max On Time'
        self._state = None
        self._device = device
        self._device_id = device.id + '_max_on_time'
        self._sauna = sauna
        self._attr_unique_id = device.id + '_max_on_time'
        self._attr_icon = 'mdi:timer-sand'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        if self._state is None:
            return None
        minutes = int(self._state)
        return f"{minutes // 60:02}:{minutes % 60:02}"
    
    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        self._device.maxOnTimeSensor = self
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()

class HarviaHeatUpTimeSensor(SensorEntity):
    """Representatie van de opwarmtijd."""

    def __init__(self, device, name, sauna):
        """Initialiseer de sensor."""
        self._name = name + ' Heat Up Time'
        self._state = None
        self._device = device
        self._device_id = device.id + '_heat_up_time'
        self._sauna = sauna
        self._attr_unique_id = device.id + '_heat_up_time'
        self._attr_icon = 'mdi:chart-timeline-variant'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        if self._state is None:
            return None
        minutes = int(self._state)
        return f"{minutes // 60:02}:{minutes % 60:02}"

    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        self._device.heatUpTimeSensor = self
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()

class HarviaRelayCounterSensor(SensorEntity):
    """Representatie van de relais schakelteller."""

    def __init__(self, device, name, sauna, phase):
        """Initialiseer de sensor."""
        self._name = f"{name} Relay {phase.replace('ph', '')} Counter"
        self._state = None
        self._device = device
        self._device_id = device.id + f"_relay_{phase}_counter"
        self._sauna = sauna
        self._attr_unique_id = device.id + f"_relay_{phase}_counter"
        self._attr_icon = 'mdi:counter'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        return self._state

    @property
    def state_class(self):
        return "measurement"

    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        # Registratie gebeurt in __init__ in de loop
        # self._device.relayCounterSensors.append(self)
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()

class HarviaSteamerCounterSensor(SensorEntity):
    """Representatie van de steamer teller."""

    def __init__(self, device, name, sauna):
        """Initialiseer de sensor."""
        self._name = name + ' Steamer Counter'
        self._state = None
        self._device = device
        self._device_id = device.id + '_steamer_counter'
        self._sauna = sauna
        self._attr_unique_id = device.id + '_steamer_counter'
        self._attr_icon = 'mdi:counter'

    @property
    def name(self):
        """Return de naam van de sensor."""
        return self._name

    @property
    def state(self):
        """Return de staat van de sensor."""
        return self._state

    @property
    def state_class(self):
        return "measurement"

    async def async_added_to_hass(self):
        """Acties die uitgevoerd moeten worden als entiteit aan HA is toegevoegd."""
        self._device.steamerCounterSensor = self
        await self._device.update_ha_devices()

    async def update_state(self):
        self.async_write_ha_state()


    #@property
    #def device_info(self):
    #    """Return informatie over het aangesloten apparaat."""
    #    return {
    #        "identifiers": {(DOMAIN, self._device.id)},
    #        "name": self._device.name,
    #        "manufacturer": "Harvia",
    #    }

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up de Harvia sensors."""
    devices = await hass.data[DOMAIN]['api'].get_devices()
    all_sensors = []  # Gebruik een andere variabele om verwarring te voorkomen

    for device in devices:
        _LOGGER.debug(f"Loading sensors for device: {device.name}")
        device_sensors = await device.get_sensors()  # Verkrijg  sensors voor het huidige apparaat
        all_sensors.extend(device_sensors)  # Voeg de verkregen sensors toe aan de lijst

    async_add_entities(all_sensors, True)