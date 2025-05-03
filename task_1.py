from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

def main():
    # Create an optimization model
    model = LpProblem(name="beverage-production", sense=LpMaximize)

    # Define decision variables
    lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
    fruit_juice = LpVariable(name="FruitJuice", lowBound=0, cat='Integer')

    # Define the objective function (maximize the total number of products)
    model += lpSum([lemonade, fruit_juice]), "Total products"

    # Define constraints
    model += (2 * lemonade + 1 * fruit_juice <= 100, "Water constraint")
    model += (1 * lemonade <= 50, "Sugar constraint")
    model += (1 * lemonade <= 30, "Lemon juice constraint")
    model += (2 * fruit_juice <= 40, "Fruit puree constraint")

    # Solve the model
    model.solve()

    # Output results
    print(f"Status: {LpStatus[model.status]}")
    print(f"\nOptimal solution:")
    print(f"Produce Lemonade: {lemonade.value():.0f} units")
    print(f"Produce Fruit Juice: {fruit_juice.value():.0f} units")
    print(f"Total number of products: {lemonade.value() + fruit_juice.value():.0f} units")
    
    # Output resource usage
    print("\nResource usage:")
    print(f"Water: {2 * lemonade.value() + 1 * fruit_juice.value():.0f} units out of 100")
    print(f"Sugar: {1 * lemonade.value():.0f} units out of 50")
    print(f"Lemon juice: {1 * lemonade.value():.0f} units out of 30")
    print(f"Fruit puree: {2 * fruit_juice.value():.0f} units out of 40")

if __name__ == "__main__":
    main()
