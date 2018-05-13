""" This module contains functions capable of modifying and shaping the Genome"""

import universal_functions
import datetime
import random
import string


class GeneModifier:
    def change_cortical_neuron_count(self, cortical_area, change_percentage):
        """ Function to increase or decrease the neuron density aka Cortical Neuron Count in a given cortical area"""
        universal_functions.genome['blueprint'][cortical_area]['cortical_neuron_count'] += \
            universal_functions.genome['blueprint'][cortical_area]['cortical_neuron_count'] * change_percentage
        return

    def change_firing_threshold(self, cortical_area, change_percentage):
        """ Function to increase or decrease the neuron firing threshold in a given cortical area"""
        universal_functions.genome['blueprint'][cortical_area]['neuron_params']['firing_threshold'] += \
            universal_functions.genome['blueprint'][cortical_area]['neuron_params']['firing_threshold'] * change_percentage
        return

    def change_depolarization_timer_threshold(self, cortical_area, change_percentage):
        """ Function to increase or decrease the neuron timer threshold in a given cortical area"""
        universal_functions.genome['blueprint'][cortical_area]['neuron_params']['depolarization_timer_threshold'] += \
            universal_functions.genome['blueprint'][cortical_area]['neuron_params']['depolarization_timer_threshold'] * change_percentage
        return

    def change_consecutive_fire_cnt_max(self, cortical_area, change_percentage):
        """ Function to increase or decrease the neuron consecutive_fire_cnt_max in a given cortical area"""
        universal_functions.genome['blueprint'][cortical_area]['neuron_params']['consecutive_fire_cnt_max'] += \
            universal_functions.genome['blueprint'][cortical_area]['neuron_params']['consecutive_fire_cnt_max'] * change_percentage
        return

    def change_snooze_length(self, cortical_area, change_percentage):
        """ Function to increase or decrease the neuron snooze_length in a given cortical area"""
        universal_functions.genome['blueprint'][cortical_area]['neuron_params']['snooze_length'] += \
            universal_functions.genome['blueprint'][cortical_area]['neuron_params']['snooze_length'] * change_percentage
        return


def genome_id_gen(size=6, chars=string.ascii_uppercase + string.digits):
    """
    This function generates a unique id which will be associated with each GEnome

    """
    # Rand gen source partially from:
    # http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    return str(datetime.datetime.now()).replace(' ', '_')+'_'+(''.join(random.choice(chars) for _ in range(size)))+'_G'


def generation_assessment():
    """ A collection of assessments to evaluate the performance of the Genome"""
    return


def genethesize():
    """ Responsible for generating a complete set of Genome"""

    genome = {}
    genome["firing_patterns"] = {
      "A": {
         "frequency": "100",
         "magnitude": "80"
      },
      "B": {
         "frequency": "20",
         "magnitude": "100"
      }
   }
    genome["neighbor_locator_rule"] = {
      "rule_0": {
         "param_1": 5,
         "param_2": 0
      },
      "rule_1": {
         "param_1": 5,
         "param_2": 5
      },
      "rule_2": {
         "param_1": 5,
         "param_2": 5,
         "param_3": 10
      },
      "rule_3": {
         "param_1": 0,
         "param_2": 0
      }
   }
    return genome


def genome_selector():
    genome_id = universal_functions.genome_metadata["most_recent_genome_id"]
    return genome_id


def mutate():
    return


def crossover():
    return


def translate_genotype2phenotype():
    return


def calculate_fitness():
    return


def calculate_survival_prob():
    return


def synthesize_new_gen():
    return


def selection():
    return


def spin_new_generation():
    return

# print(genethesize())