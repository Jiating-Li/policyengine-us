from policyengine_us.model_api import *


class dc_tanf_countable_gross_unearned_income(Variable):
    value_type = float
    entity = SPMUnit
    label = "DC TANF countable gross unearned income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.DC

    def formula(spm_unit, period, parameters):
        p = parameters(period).gov.states.dc.dhs.tanf.income
        # Sum unearned sources, plus child support disregard $150 received per month.
        gross_unearned = add(spm_unit, period, p.unearned)
        child_support = add(spm_unit, period, ["child_support_received"])
        return gross_unearned + max_(child_support - 150 * 12, 0)
