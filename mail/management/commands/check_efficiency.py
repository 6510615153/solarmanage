# mail/management/commands/check_efficiency.py

from django.core.management.base import BaseCommand
from mainapp.models import SolarPlant, SolarPanel 
from mail.utils import send_custom_email 
import logging

logger = logging.getLogger(__name__) 

class Command(BaseCommand):
    help = 'Checks solar plant efficiency and sends alerts if average panel energy is below 80% of standard.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting solar plant efficiency check..."))

        STANDARD_PANEL_ENERGY = 5000 # defined standard for panel_energy
        EFFICIENCY_THRESHOLD_PERCENT = 80
        # Calculate the actual energy threshold based on percentage
        ENERGY_THRESHOLD = (EFFICIENCY_THRESHOLD_PERCENT / 100) * STANDARD_PANEL_ENERGY # 0.80 * 5000 = 4000

        try:
            all_plants = SolarPlant.objects.all()

            if not all_plants.exists():
                self.stdout.write("No solar plants found in the database. Exiting.")
                return

            for plant in all_plants:
                self.stdout.write(f"\nChecking plant: {plant.plant_name} (Code: {plant.plant_code})")

                panels = plant.plant_panels.all()
                total_panels = panels.count()

                if total_panels == 0:
                    self.stdout.write(f"  No panels found for this plant. Skipping efficiency check.")
                    continue

                # Calculate the sum of current panel energies
                current_total_energy = sum(panel.panel_energy for panel in panels)
                
                # Calculate the average panel energy for this plant
                average_panel_energy = current_total_energy / total_panels

                self.stdout.write(f"  Average panel energy: {average_panel_energy:.2f} (Standard: {STANDARD_PANEL_ENERGY})")
                self.stdout.write(f"  Threshold for 80% efficiency: {ENERGY_THRESHOLD:.2f}")

                if average_panel_energy < ENERGY_THRESHOLD:
                    self.stdout.write(self.style.WARNING(f"  Alert: Average panel energy ({average_panel_energy:.2f}) is below {EFFICIENCY_THRESHOLD_PERCENT}% of standard!"))

                    manager_member = plant.plant_owner
                    manager_user = manager_member.member_user
                    manager_email = manager_user.email

                    subject = f"Low Efficiency Alert: {plant.plant_name} ({plant.plant_code})"
                    message = (
                        f"Dear {manager_user.first_name if manager_user.first_name else manager_user.username},\n\n"
                        f"This is an automated alert from your Solar Monitoring System.\n"
                        f"The solar plant '{plant.plant_name}' (Code: {plant.plant_code}) is currently operating "
                        f"with an average panel energy of {average_panel_energy:.2f}, which is below the "
                        f"{EFFICIENCY_THRESHOLD_PERCENT}% threshold ({ENERGY_THRESHOLD:.2f}) of the standard {STANDARD_PANEL_ENERGY}.\n\n"
                        f"Please log in to the system for more details and to take appropriate action.\n\n"
                        f"Best regards,\nYour Solar System Team"
                    )

                    # Send the email using your utility function
                    email_sent = send_custom_email(subject, message, manager_email)

                    if email_sent:
                        self.stdout.write(self.style.SUCCESS(f"  Alert email successfully sent to {manager_email}."))
                    else:
                        self.stdout.write(self.style.ERROR(f"  Failed to send alert email to {manager_email}. Check logs for details."))
                else:
                    self.stdout.write(self.style.SUCCESS(f"  Plant operating above {EFFICIENCY_THRESHOLD_PERCENT}% threshold. No alert needed."))

        except Exception as e:
            logger.error(f"An unexpected error occurred during efficiency check: {e}", exc_info=True)
            self.stdout.write(self.style.ERROR(f"An unexpected error occurred: {e}"))

        self.stdout.write(self.style.SUCCESS('\nSolar plant efficiency check complete.'))