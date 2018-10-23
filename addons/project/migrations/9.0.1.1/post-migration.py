# -*- coding: utf-8 -*-
# @ 2014-Today: Odoo Community Association, Microcom
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def map_priority(cr):
    openupgrade.map_values(
        cr,
        openupgrade.get_legacy_name('priority'),
        'priority',
        [('2', '1')],
        table='project_task', write='sql')


def map_template_state(cr):
    openupgrade.map_values(
        cr,
        openupgrade.get_legacy_name('state'),
        'state',
        [('template', 'draft')],
        table='project_project', write='sql')


def copy_user_id(cr):
    openupgrade.logged_query(cr, """
        UPDATE project_project p
        SET user_id = a.user_id
        FROM account_analytic_account a
        WHERE a.id = p.analytic_account_id
        """)


def copy_dates(cr):
    openupgrade.logged_query(cr, """
        UPDATE project_project p
        SET (date, date_start) = (a.%s, a.%s)
        FROM account_analytic_account a
        WHERE a.id = p.analytic_account_id
        """ % (openupgrade.get_legacy_name('date'),
               openupgrade.get_legacy_name('date_start_bk')))


def create_project_for_account(env):
    """Create a project for an already existing analytic account."""
    env.cr.execute("""
    SELECT aa.id, aa.complete_wbs_name, aa.complete_wbs_code
    FROM account_analytic_account aa
    LEFT JOIN project_project pp ON pp.analytic_account_id = aa.id
    WHERE pp.analytic_account_id is null;
    """)
    acc_ids = env.cr.fetchall()
    acc_model = env['account.analytic.account']
    project_model = env['project.project']
    accs = acc_model.browse([x[0] for x in acc_ids])
    for this in accs:
        project_model.create({
            'name': this.name,
            'analytic_account_id': this.id,
            'account_class': u'project',
        })


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    cr = env.cr
    map_priority(cr)
    map_template_state(cr)
    copy_user_id(cr)
    openupgrade.convert_field_to_html(
        cr, 'project_task', openupgrade.get_legacy_name('description'),
        'description'
    )
    openupgrade.load_data(
        cr, 'project', 'migrations/9.0.1.1/noupdate_changes.xml',
    )
    copy_dates(cr)
    create_project_for_account(env)
