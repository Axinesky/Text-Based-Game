from dir.slowtext import slow_text_centered
import os

def clear_screen():
    os.system('cls')


    # Assigned to temporary variables to make sure originals aren't tampered with
    goblin = list(hostile.keys())[1]
    goblin_stats = copy.deepcopy(hostile["Goblin"])

    slow_text_centered(f"You are being attacked by a {hub_boss}", min_delay=0.02, max_delay=0.12, newLine=True,
                       vertical_padding=True)
    clear_screen()
    time.sleep(1.5)
    while goblin_stats["health"] > 0:
        slow_text_centered("What would you like to do? ", min_delay=0.02, max_delay=0.12, newLine=True,
                           vertical_padding=True)
        slow_text_centered("Swing your weapon (attack)", min_delay=0.02, max_delay=0.12, newLine=True,
                           vertical_padding=False)
        slow_text_centered("Cast a spell (magic spell)", min_delay=0.02, max_delay=0.12, newLine=True,
                           vertical_padding=False)
        user_choice = input("> ").capitalize()
        clear_screen()  # Failsafe terminal clean incase function one doesn't work
        temporary_player_health, temporary_enemy_health = combat_system(goblin_stats, user_choice, goblin)
        goblin_stats["health"] = temporary_enemy_health  # Update fight turn info
        player["health"] = temporary_player_health
        if temporary_enemy_health < 0:  # Kill check
            clear_screen()
            slow_text_centered(f"You have killed {goblin}!", min_delay=0.02, max_delay=0.08, newLine=True,
                               vertical_padding=True)
            health_refresh()
            slow_text_centered(f"You gained 1 XP", min_delay=0.02, max_delay=0.08, newLine=True, vertical_padding=False)
            slow_text_centered(f"The slime spat out a weapon from a fallen Hub Soldier", min_delay=0.02, max_delay=0.08,
                               newLine=True, vertical_padding=False)