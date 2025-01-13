# This file is part of the faebryk project
# SPDX-License-Identifier: MIT

import logging

import faebryk.library._F as F  # noqa: F401
from faebryk.core.module import Module
from faebryk.libs.library import L  # noqa: F401
from faebryk.libs.picker.picker import DescriptiveProperties
from faebryk.libs.units import P  # noqa: F401

logger = logging.getLogger(__name__)


class SP3243E(Module):
    """
    250Kbps RS232 Transceiver 3tx/5rx SSOP28
    """

    def enable_chip(self):
        self.enable.set(on=True)

    def enable_auto_online(self):
        self.online.set(on=False)

    # ----------------------------------------
    #     modules, interfaces, parameters
    # ----------------------------------------
    voltage_doubler_charge_pump_power: F.ElectricPower
    """Terminal of the voltage doubler charge-pump capacitor """
    inverting_charge_pump_power: F.ElectricPower
    """Terminal of the inverting charge-pump capacitor """
    positive_charge_pump_power: F.ElectricPower
    """Regulated +5.5V output generated by the charge pump """
    negative_charge_pump_power: F.ElectricPower
    """Regulated -5.5V output generated by the charge pump """
    power: F.ElectricPower
    """Power input to the module"""

    uart: F.UART
    rs232: F.RS232

    enable: F.ElectricLogic
    online: F.ElectricLogic
    status: F.ElectricLogic

    cts_inverted: F.ElectricLogic

    # ----------------------------------------
    #                 traits
    # ----------------------------------------
    designator_prefix = L.f_field(F.has_designator_prefix)(
        F.has_designator_prefix.Prefix.U
    )
    datasheet = L.f_field(F.has_datasheet_defined)(
        "https://assets.maxlinear.com/web/documents/sp3243e.pdf"
    )

    @L.rt_field
    def descriptive_properties(self):
        return F.has_descriptive_properties_defined(
            {
                DescriptiveProperties.manufacturer: "MaxLinear",
                DescriptiveProperties.partno: "SP3243EBEA-L/TR",
            },
        )

    @L.rt_field
    def pin_association_heuristic(self):
        return F.has_pin_association_heuristic_lookup_table(
            mapping={
                self.inverting_charge_pump_power.hv: ["C2+"],
                self.rs232.rts.signal: ["T2OUT"],
                self.rs232.dtr.signal: ["T3OUT"],
                self.uart.dtr.signal: ["T3IN"],
                self.uart.rts.signal: ["T2IN"],
                self.uart.base_uart.tx.signal: ["T1IN"],
                self.uart.ri.signal: ["R5OUT"],
                self.uart.dcd.signal: ["R4OUT"],
                self.uart.dsr.signal: ["R3OUT"],
                self.uart.cts.signal: ["R2OUT"],
                self.uart.base_uart.rx.signal: ["R1OUT"],
                self.inverting_charge_pump_power.lv: ["C2-"],
                self.cts_inverted.signal: ["R2OUT#"],
                self.status.signal: ["STATUS#"],
                self.enable.signal: ["SHUTDOWN#"],
                self.online.signal: ["ONLINE#"],
                self.voltage_doubler_charge_pump_power.lv: ["C1-"],
                self.power.lv: ["GND"],
                self.power.hv: ["VCC"],
                self.positive_charge_pump_power.hv: ["V+"],
                self.voltage_doubler_charge_pump_power.hv: ["C1+"],
                self.negative_charge_pump_power.lv: ["V-"],
                self.rs232.rx.signal: ["R1IN"],
                self.rs232.cts.signal: ["R2IN"],
                self.rs232.dsr.signal: ["R3IN"],
                self.rs232.dcd.signal: ["R4IN"],
                self.rs232.ri.signal: ["R5IN"],
                self.rs232.tx.signal: ["T1OUT"],
            },
            accept_prefix=False,
            case_sensitive=False,
        )

    def __preinit__(self):
        # ------------------------------------
        #          parametrization
        # ------------------------------------
        self.power.voltage.constrain_subset(L.Range(3.0 * P.V, 5.5 * P.V))

        self.uart.base_uart.baud.constrain_le(250 * P.kbaud)

        self.rs232.get_trait(
            F.has_single_electric_reference
        ).get_reference().voltage.constrain_subset(
            L.Range.from_center(3 * P.V, 15 * P.V)
        )  # TODO: Support negative numbers (-15 * P.V, 15 * P.V))

        # ------------------------------------
        #           connections
        # ------------------------------------
        F.ElectricLogic.connect_all_module_references(self, exclude=[self.rs232])

        # ------------------------------------
        #          parametrization
        # ------------------------------------
        self.power.voltage.constrain_subset(L.Range(3.0 * P.V, 5.5 * P.V))
