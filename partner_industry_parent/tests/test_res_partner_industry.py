# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.base.tests.common import BaseCommon


class TestResPartnerIndustry(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.industry_1 = cls.env.ref("base.res_partner_industry_O")
        cls.industry_2 = cls.env.ref("base.res_partner_industry_P")
        cls.industry_3 = cls.env.ref("base.res_partner_industry_Q")

    def test_res_partner_industry_complete_name(self):
        self.assertEqual(self.industry_1.complete_name, "Public Administration")
        self.industry_1.parent_id = self.industry_2
        self.assertEqual(
            self.industry_1.complete_name, "Education / Public Administration"
        )
        self.industry_2.parent_id = self.industry_3
        self.assertEqual(
            self.industry_1.complete_name,
            "Health/Social / Education / Public Administration",
        )
