def myfunction(n):
    # First Loop
    for i in range(0, n+1):
        print("First Loop")

    # Second Loop
    j = 1
    while j <= n+1:
        print("Second Loop", j)
        j = j * 2

    # Third Loop
    for i in range(0, 100):
        print("Third Loop")

    # Printing Time Complexities
    print("\nTime Complexity of First Loop: O(n)")
    print("Time Complexity of Second Loop: O(log n)")
    print("Time Complexity of Third Loop: O(1)")
    print("Overall Time Complexity: O(n)")


# Example call
myfunction(10)
