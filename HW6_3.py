# Region Imports
from Rankine_stem import rankine
# End Region

def main():
    # Scenario 1: Saturated vapor entering the turbine
    rankine_cycle_1 = rankine(p_low=8, p_high=8000, name='Rankine Cycle: Saturated Vapor')
    efficiency_1 = rankine_cycle_1.calc_efficiency()
    print(f"Efficiency of Rankine Cycle with Saturated Vapor: {efficiency_1:.2f}%")
    rankine_cycle_1.print_summary()

    # Scenario 2: Superheated steam entering the turbine
    Tsat = 295  # Tsat Value at 8000 kPa from Steam Table
    T1 = 1.7 * Tsat  # Example temperature, replace with your actual calculated value

    rankine_cycle_2 = rankine(p_low=8, p_high=8000, t_high=T1, name='Rankine Cycle: Superheated Steam')
    efficiency_2 = rankine_cycle_2.calc_efficiency()
    print(f"Efficiency of Rankine Cycle with Superheated Steam: {efficiency_2:.2f}%")
    rankine_cycle_2.print_summary()


if __name__ == "__main__":
    main()

