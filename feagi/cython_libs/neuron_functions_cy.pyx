def neuron_update(float presynaptic_current,
                  int burst_count,
                  int last_membrane_potential_update,
                  float leak_coefficient,
                  float membrane_potential):

    if leak_coefficient > 0:
        if last_membrane_potential_update < burst_count:
            leak_window = burst_count - last_membrane_potential_update
            leak_value = leak_window * leak_coefficient
            membrane_potential -= leak_value
            if membrane_potential < 0:
                membrane_potential = 0


    membrane_potential += presynaptic_current

    return membrane_potential
