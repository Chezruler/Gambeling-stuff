import random

def randomstuff(bullets):
    population = ["💀", "🥳"]
    death_weight = bullets * 1.5
    survive_weight = (6 - bullets) * 8.3
    weights = [death_weight, survive_weight]
    return random.choices(population, weights=weights, k=1)

def kill(bullet):
    if bullet[0] == "💀":
        print("You're dead! 💀")
        return False
    elif bullet[0] == "🥳":
        print("You're alive! 🥳")
        return True

def main():
    print("Welcome to Russian Roulette, try to survive!")
    bullets = 1

    while True:
        play_input = input(f"\n[Bullet {bullets}/6] Wanna pull the trigger? (Y/N): ")

        if play_input.strip().upper() == "N":
            print("Smart choice. You walked away!")
            break
        elif play_input.strip().upper() != "Y":
            print("Please enter Y or N.")
            continue

        result = randomstuff(bullets)
        print(f"Result: {result[0]}")

        alive = kill(result)
        if not alive:
            break

        bullets += 1
        if bullets > 6:
            print("You survived all 6 rounds! Congrats! 🎉")
            break

        death_chance = round((bullets * 1.5) / (bullets * 1.5 + (6 - bullets) * 8.3) * 100, 1)
        print(f"There are now {bullets} bullets in the gun! Death chance: {death_chance}%")

if __name__ == "__main__":
    main()
