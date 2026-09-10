package com.example.backendinterview.lab.day01;

public final class ComplexityExamples {

    private ComplexityExamples() {
    }

    public static int first(int[] numbers) {
        if (numbers.length == 0) {
            throw new IllegalArgumentException("numbers must not be empty");
        }
        return numbers[0];
    }

    public static boolean containsLinear(int[] numbers, int target) {
        for (int number : numbers) {
            if (number == target) {
                return true;
            }
        }
        return false;
    }

    public static long pairCount(int[] numbers) {
        long count = 0;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers.length; j++) {
                count++;
            }
        }
        return count;
    }
}
