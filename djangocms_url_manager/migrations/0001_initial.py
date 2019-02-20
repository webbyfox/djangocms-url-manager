# Generated by Django 2.0.8 on 2018-08-30 06:47

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields

from djangocms_url_manager.models import get_templates, TEMPLATE_DEFAULT, TARGET_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = [("sites", "0002_alter_domain_unique"), ("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="LinkPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="djangocms_url_manager_linkplugin",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("label", models.CharField(max_length=120, verbose_name="label")),
                (
                    "template",
                    models.CharField(
                        choices=get_templates(), default=TEMPLATE_DEFAULT, max_length=255, verbose_name="Template"
                    ),
                ),
                ("target", models.CharField(blank=True, choices=TARGET_CHOICES, max_length=255, verbose_name="Target")),
                (
                    "attributes",
                    djangocms_attributes_field.fields.AttributesField(
                        blank=True, default=dict, verbose_name="Attributes"
                    ),
                ),
            ],
            options={"verbose_name": "url plugin model", "verbose_name_plural": "url plugin models"},
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="Url",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "manual_url",
                    models.URLField(
                        blank=True,
                        help_text="Provide a valid URL to an external website.",
                        max_length=2040,
                        verbose_name="manual URL",
                    ),
                ),
                ("object_id", models.PositiveIntegerField(null=True)),
                (
                    "anchor",
                    models.CharField(
                        blank=True,
                        help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.',
                        max_length=255,
                        verbose_name="anchor",
                    ),
                ),
                ("mailto", models.EmailField(blank=True, max_length=255, verbose_name="email address")),
                ("phone", models.CharField(blank=True, max_length=255, verbose_name="phone")),
                (
                    "content_type",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="contenttypes.ContentType"
                    ),
                ),
                ("site", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="sites.Site")),
            ],
            options={"verbose_name": "url", "verbose_name_plural": "urls"},
        ),
        migrations.CreateModel(
            name="UrlOverride",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "manual_url",
                    models.URLField(
                        blank=True,
                        help_text="Provide a valid URL to an external website.",
                        max_length=2040,
                        verbose_name="manual URL",
                    ),
                ),
                ("object_id", models.PositiveIntegerField(null=True)),
                (
                    "anchor",
                    models.CharField(
                        blank=True,
                        help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.',
                        max_length=255,
                        verbose_name="anchor",
                    ),
                ),
                ("mailto", models.EmailField(blank=True, max_length=255, verbose_name="email address")),
                ("phone", models.CharField(blank=True, max_length=255, verbose_name="phone")),
                (
                    "content_type",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="contenttypes.ContentType"
                    ),
                ),
                ("site", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="sites.Site")),
                ("url", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="djangocms_url_manager.Url")),
            ],
            options={"verbose_name": "url override", "verbose_name_plural": "url overrides"},
        ),
        migrations.AddField(
            model_name="linkplugin",
            name="url",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cms_plugins",
                to="djangocms_url_manager.Url",
                verbose_name="url",
            ),
        ),
        migrations.AlterUniqueTogether(name="urloverride", unique_together={("site", "url")}),
    ]
