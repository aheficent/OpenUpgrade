""" Encode any known changes to the database here
to help the matching process
"""

renamed_modules = {

    # OCA/product-attribute
    'product_m2m_categories': 'product_multi_category',
    # OCA/e-commerce
    'product_links': 'product_multi_link',
    # OCA/sale-workflow
    # OCA/partner-contact
    'partner_external_maps': 'partner_external_map',

    # OCA/server-tools
    # OCA/runbot-addons
    'runbot_secure': 'runbot_relative',
    # not exactly a module rename, but they do the same

    # OCA/account-invoicing
    'account_refund_original': 'account_invoice_refund_link',
    # 'stock_dropshipping_dual_invoice': 'stock_dropshipping',
    # OCA/stock-logistics-workflow
    'stock_picking_reorder_lines': 'stock_picking_line_sequence',
    # OCA/purchase-workflow
    # OCA/social
    'mail_message_name_search': 'base_search_mail_content',
    'marketing_security_group': 'mass_mailing_security_group',
    # odoomrp/odoomrp-wip
    'product_variants_no_automatic_creation': 'product_variant_configurator',
    'sale_product_variants': 'sale_variant_configurator',
    'sale_stock_product_variants': 'sale_stock_variant_configurator',
    # OCA/account-financial-reporting

    # OCA/contract
    'contract_recurring_plans': 'contract_recurring_analytic_distribution',
    # OCA/website
    'website_disable_odoo': 'website_odoo_debranding',
    # OCA/account-analytic

    # OCA/project
    # OCA/manufacture-reporting
    'mrp_bom_structure_xls_level_1': 'mrp_bom_structure_xlsx_level_1',
    # OCA/l10n-spain
    'l10n_es_fiscal_year_closing': 'l10n_es_account_fiscal_year_closing',
    'account_balance_reporting_xls': 'account_balance_reporting_xlsx',

    # stock-logistics-barcode
    'product_barcode_generator': 'barcodes_generator_product',
    #l10n
    'l10n_es_account_financial_report': 'account_journal_report',
    #reporting-engine
    # 'report_xls': 'report_xlsx',
    'website_sale_collapse_categories': 'website_sale',
    'website_event_register_free': 'website_event',
    'website_event_register_free_with_sale': 'website_event_sale',
    'account_payment_sale_stock': 'account_payment_sale',
    # 'sale_order_line_dates': 'sale_order_line_date',
    # 'sale_documents_comments': 'sale_comment_propagation',
}

renamed_models = {
}
