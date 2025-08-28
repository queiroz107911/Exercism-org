"""

Functions to prevent a nuclear meltdown.
In this exercise, we'll develop a simple control system for a nuclear reactor

"""


def is_criticality_balanced(temperature, neutrons_emitted):

    """Verify criticality is balanced

    :param temperature: int or float - temperature value in kelvin
    :param neutrons_emitted: int or float - number of neutrons emitted per second
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K
    - The number of neutrons emitted per second is greater than 500
    - The product of temperature and neutrons emitted per second is less than 500000

    """

    # is critical if:
    # The temperature is less than 800 K
    # The number of neutrons emitted per second is greater than 500
    # The product of temperature and neutrons emitted per second is less than 500000

    if temperature > 800 and neutrons_emitted < 500 and temperature * neutrons_emitted < 500000:
        return False    # not critical
    else:
        return True     # critical
    #  if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
    #     return True    # crítico (todas condições satisfeitas)
    # else:
    #     return False   # não crítico

print('The reactor is critical: ', is_criticality_balanced(750, 600))
print('-'*30)


def reactor_efficiency(voltage, current, theoretical_max_power):

    """Assess reactor efficiency zone

    :param voltage: int or float - voltage value
    :param current: int or float - current value
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency
    :return: str - one of ('green', 'orange', 'red', or 'black')

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current

    """
    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power)*100

    if percentage_value >= 80:
        return 'green'
    elif percentage_value >= 60:
        return 'orange'
    elif percentage_value >= 30:
        return 'red'
    else:
        return 'black'

print('Reactor_efficiency: ', reactor_efficiency(200, 50, 15000))
print('-'*30)


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    product = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold

    if product < lower_bound:
        return 'LOW'
    if lower_bound <= product <= upper_bound:
        return 'NORMAL'
    return 'DANGER'

print('Fail safe: ', fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))

