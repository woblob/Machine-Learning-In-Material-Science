unitsMap = {
    "bulk_modulus": "[GPa]",
    "shear_modulus": "[GPa]",
    "homogeneous_poisson": "[-]",
    "universal_anisotropy": "[-]",
}

featureMap = {
    "bulk_modulus": "Moduł sprężystości objętościowej",
    "shear_modulus": "Moduł sprężystości poprzecznej",
    "homogeneous_poisson": "Liczba Poisson'a",
    "universal_anisotropy": "Współczynnik anizotropii",
}

bounds = {
    "bulk_modulus": ([0, 400], [0, 400]),
    "shear_modulus": ([0, 250], [0, 250]),
    "universal_anisotropy": ([0, 3], [0, 3]),
    "homogeneous_poisson": ([0, 0.5], [0, 0.5]),
}
