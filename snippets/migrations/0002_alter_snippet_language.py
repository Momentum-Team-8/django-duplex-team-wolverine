# Generated by Django 3.2.4 on 2021-06-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('html', 'HTML'), ('css', 'CSS'), ('javascript', 'JavaScript'), ('bash', 'Bash'), ('cpp', 'C++'), ('django', 'Django'), ('git', 'Git'), ('http', 'HTTP'), ('gitignore', '.ignore'), ('json', 'JSON'), ('php', 'PHP'), ('python', 'Python'), ('jsx', 'React JSX'), ('regex', 'Regex'), ('rest', 'reST'), ('ruby', 'Ruby'), ('sql', 'SQL')], max_length=25),
        ),
    ]
