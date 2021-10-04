from django.core.management.base import BaseCommand, CommandError
from shoes.models import ShoeColor, ShoeType

class Command(BaseCommand):
    help = 'Populates the shoe type and shoe color tables'

    def add_arguments(self, parser):
        parser.add_argument('shoe_ids', nargs='?', type=int)

    def handle(self, *args, **options):
        shoe_types = ["sneaker", "boot", "sandal", "dress", "other"]
        shoe_colors = ["Red,"  "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White", "Black"]
        for color in shoe_colors:
            new_color = ShoeColor(color_name = color)
            new_color.save()
        for type in shoe_types:
            new_type = ShoeType(style = type)
            new_type.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully added colors and types'))