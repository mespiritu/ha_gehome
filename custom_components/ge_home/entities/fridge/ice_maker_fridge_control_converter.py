from gehomesdk import ErdOnOff, IceMakerControlStatus

class IceMakerFridgeControlConverter:
    """Converter for fridge ice maker"""

    def boolify(self, value: IceMakerControlStatus) -> bool:
        """Convert fridge ice maker status"""
        return value.status_fridge == ErdOnOff.ON

    def true_value(self) -> IceMakerControlStatus:
        """True state"""
        return IceMakerControlStatus(ErdOnOff.ON, ErdOnOff.NA)

    def false_value(self) -> IceMakerControlStatus:
        """False state"""
        return IceMakerControlStatus(ErdOnOff.OFF, ErdOnOff.NA)
