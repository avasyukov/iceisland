from typing import List


class Layer:
    """"""

    def __init__(self, h: float, rho: float, young_modulus: float, shear_modulus: float):
        self._h = h
        self._rho = rho
        self._young_modulus = young_modulus
        self._shear_modulus = shear_modulus

    @property
    def h(self):
        return self._h

    @property
    def rho(self):
        return self._rho

    @property
    def young_modulus(self):
        return self._young_modulus

    @property
    def shear_modulus(self):
        return self._shear_modulus

    def __repr__(self):
        return '<Layer h={h} rho={rho} young_modulus={young_modulus} shear_modulus={shear_modulus}>'.format(
            h=self.h, rho=self.rho,
            young_modulus=self.young_modulus, shear_modulus=self.shear_modulus,
        )


class Base:
    def __init__(self, layers: List[Layer]):
        self._layers = layers

    @property
    def layers(self) -> List[Layer]:
        return self._layers

    def __repr__(self) -> str:
        return '<Base layers={}>'.format(self.layers)