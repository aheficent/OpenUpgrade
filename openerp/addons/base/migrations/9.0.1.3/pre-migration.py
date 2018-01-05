# -*- coding: utf-8 -*-
# Copyright Stephane LE CORNEC
# Copyright 2017 Tecnativa - Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade
from openerp.addons.openupgrade_records.lib import apriori


column_copies = {
    'ir_actions': [
        ('help', None, None),
    ],
    'ir_ui_view': [
        ('arch', 'arch_db', None),
    ],
    'res_partner': [
        ('type', None, None),
    ]
}

field_renames = [
    ('res.partner.bank', 'res_partner_bank', 'bank', 'bank_id'),
    # renamings with oldname attribute - They also need the rest of operations
    ('res.partner', 'res_partner', 'ean13', 'barcode'),
]


OBSOLETE_RULES = (
    'multi_company_default_rule',
    'res_currency_rule',
)


def remove_obsolete(cr):
    openupgrade.logged_query(cr, """
        delete from ir_rule rr
        using ir_model_data d where rr.id=d.res_id
        and d.model = 'ir.rule' and d.module = 'base'
        and d.name in {}
        """.format(OBSOLETE_RULES))


def cleanup_modules(cr):
    """Don't report as missing these modules, as they are integrated in
    other modules."""
    openupgrade.update_module_names(
        cr, [
            #from apriori
            # OCA/product-attribute
            ('product_m2m_categories', 'product_multi_category'),
            # OCA/e-commerce
            # OCA/sale-workflow
            # OCA/partner-contact
            ('partner_external_maps', 'partner_external_map'),
            #
            # # OCA/server-tools
            # # OCA/runbot-addons
            ('runbot_secure', 'runbot_relative'),
            # # not exactly a module rename, but they do the same
            #
            # # OCA/account-invoicing
            ('account_refund_original', 'account_invoice_refund_link'),
            #
            # # OCA/stock-logistics-workflow
            #
            # # OCA/purchase-workflow
            # # OCA/social
            ('mail_message_name_search', 'base_search_mail_content'),
            ('marketing_security_group', 'mass_mailing_security_group'),
            # # odoomrp/odoomrp-wip
            ('product_variants_no_automatic_creation', 'product_variant_configurator'),
            ('sale_product_variants', 'sale_variant_configurator'),
            ('sale_stock_product_variants', 'sale_stock_variant_configurator'),
            # # OCA/account-financial-reporting
            #
            # # OCA/contract
            ('contract_recurring_plans', 'contract_recurring_analytic_distribution'),
            # # OCA/website
            ('website_disable_odoo', 'website_odoo_debranding'),
            # # OCA/account-analytic
            #
            # # OCA/project
            # # OCA/manufacture-reporting
            ('mrp_bom_structure_xls_level_1', 'mrp_bom_structure_xlsx_level_1'),
            # # OCA/l10n-spain
            ('l10n_es_fiscal_year_closing', 'l10n_es_account_fiscal_year_closing'),
            ('account_balance_reporting_xls', 'account_balance_reporting_xlsx'),
            #
            # # stock-logistics-barcode
            ('product_barcode_generator', 'barcodes_generator_product'),

            ('sale_multi_picking_by_requested_date', 'sale_procurement_group_by_requested_date'),
            ('account_chart', 'account'),
            ('account_followup', 'account_credit_control'),
            ('contacts', 'mail'),
            ('marketing_crm', 'crm'),
            ('email_template', 'mail'),  # mail_template class
            ('procurement_jit_stock', 'procurement_jit'),
            ('web_gantt', 'web'),
            ('web_graph', 'web'),
            ('web_kanban_sparkline', 'web'),
            ('web_tests', 'web'),
            ('website_report', 'report'),
            ('portal_claim', 'website_crm_claim'),
            ('stock_picking_backorders', 'stock_picking_show_backorder'),
            ('purchase_analytic_plans', 'purchase_analytic_distribution'),
            ('purchase_order_reorder_lines', 'purchase_order_line_sequence'),
            ('purchase_order_line_sequence_propagate', 'purchase_order_line_sequence'),
            ('purchase_order_line_seq','purchase_order_line_sequence'),
            ('sale_analytic_plans', 'sale_analytic_distribution'),
            ('mrp_bom_structure_xls', 'mrp_bom_structure_xlsx'),
            ('account_analytic_plan_required', 'account_analytic_distribution_required'),
            ('partner_relations', 'partner_multi_relation'),
            ('account_analytic_plans', 'account_analytic_distribution'),
            ('purchase_product_variants', 'purchase_variant_configurator'),
            ('account_analytic_analysis', 'contract'),
            ('product_links', 'product_multi_link'),
            # core
            ('website_mail_group', 'website_mail_channel'),
            ('inactive_session_timeout', 'auth_session_timeout'),
            # OCA/project
            ('project_work_time_control', 'project_timesheet_time_control'),
            # OCA/account-financial-reporting
            ('account_financial_report_webkit', 'account_financial_report_qweb'),
            ('account_journal_report_xls', 'account_journal_report'),
            # same here, whoever want this will also need bank-payment
            ('account_payment', 'account_payment_order'),
            # OCA/account-invoicing
            ('account_invoice_reorder_lines', 'account_invoice_line_sequence'),
            ('account_invoice_reorder_lines', 'account_invoice_line_sequence'),
            ('stock_dropshipping_dual_invoice', 'stock_dropshipping'),
            # from OCA/account-financial-tools - Features changed
            ('account_move_line_no_default_search', 'account'),
            ('account_tax_chart_interval', 'account'),
            ('invoice_fiscal_position_update', 'account_invoice_fiscal_position_update'),
            # from OCA/account-financial-reporting
            ('account_journal_report_xls', 'account_journal_report'),
            ('account_financial_report_webkit_xls',
             'account_financial_report_qweb'),
            ('account_tax_report_no_zeroes', 'account'),
            # from OCA/account_payment
            ('account_payment_term_multi_day',
             'account_payment_term_extension'),
            ('account_check_writing', 'account_check_printing'),
            # from OCA/bank-statement-reconcile
            ('account_easy_reconcile', 'account_mass_reconcile'),
            ('account_advanced_reconcile', 'account_mass_reconcile'),
            ('account_bank_statement_period_from_line_date', 'account'),
            # from OCA/connector-telephony
            ('asterisk_click2dial_crm', 'crm_phone'),
            # from OCA/server-tools - features included now in core
            ('base_concurrency', 'base'),
            ('base_debug4all', 'base'),
            ('disable_openerp_online', 'disable_odoo_online'),
            ('cron_run_manually', 'base'),
            ('shell', 'base'),
            # from OCA/social - included in core
            ('website_mail_snippet_table_edit', 'mass_mailing'),
            ('mass_mailing_sending_queue', 'mass_mailing'),
            ('website_mail_snippet_bg_color',
             'web_editor_background_color'), # this one now located in OCA/web
            # from OCA/crm - included in core
            ('crm_lead_lost_reason', 'crm'),
            # OCA/hr
            ('hr_expense_analytic_plans', 'hr_expense_analytic_distribution'),
            # from OCA/sale-workflow - included in core
            ('sale_exceptions', 'sale_exception'),
            ('sale_order_back2draft', 'sale'),
            ('partner_prepayment', 'sale_delivery_block'),
            ('sale_fiscal_position_update', 'sale'),
            ('sale_documents_comments', 'sale_comment_propagation'),

            # ('account_voucher', 'account_voucher_payment'), # aheficent

            # ('sale_order_line_dates', 'sale_order_line_date'),
            # from OCA/bank-payment
            # ('account_payment_sale_stock', 'account_payment_sale'),
            # from OCA/website
            # ('website_event_register_free', 'website_event'),
            # ('website_event_register_free_with_sale', 'website_event_sale'),
            # ('website_sale_collapse_categories', 'website_sale'),
            # OCA/reporting-engine
            # ('report_xls', 'report_xlsx'),
            # OCA/l10n-spain
            # ('l10n_es_account_financial_report', 'account_journal_report'),
            # OCA/stock-logistics-workflow
            # ('stock_dropshipping_dual_invoice', 'stock_dropshipping'),
            # ('stock_picking_reorder_lines', 'stock_picking_line_sequence'),
            ('portal_project_issue', 'project'),
            ('crm_claim_rma', 'rma'),
        ], merge_modules=True,
    )


def map_res_partner_type(cr):
    """ The type 'default' is not an option in v9.
        By default we map it to 'contact'.
    """
    openupgrade.map_values(
        cr,
        openupgrade.get_legacy_name('type'), 'type',
        [('default', 'contact')],
        table='res_partner', write='sql')


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    cr = env.cr
    openupgrade.update_module_names(
        cr, apriori.renamed_modules.iteritems()
    )
    openupgrade.copy_columns(cr, column_copies)
    openupgrade.rename_fields(env, field_renames, no_deep=True)
    remove_obsolete(cr)
    pre_create_columns(cr)
    cleanup_modules(cr)
    map_res_partner_type(cr)

def pre_create_columns(cr):
    openupgrade.logged_query(cr, """
        alter table ir_model_fields add column compute text""")

