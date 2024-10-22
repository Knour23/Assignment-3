public class Polynomial {
    private Literal head;  // Head of the linked list

    // Constructor for an empty polynomial
    public Polynomial() {
        this.head = null;
    }

    // Method to insert a term in the correct position based on the exponent
    public void insertTerm(double coefficient, int exponent) {
        Literal newTerm = new Literal(coefficient, exponent);

        // If list is empty or new term has the highest exponent
        if (head == null || head.getExponent() < exponent) {
            newTerm.next = head;
            head = newTerm;
        } else {
            Literal current = head;
            // Traverse the list to find the correct position
            while (current.next != null && current.next.getExponent() > exponent) {
                current = current.next;
            }

            // If a term with the same exponent exists, add the coefficients
            if (current.getExponent() == exponent) {
                current.setCoefficient(current.getCoefficient() + coefficient);
            } else {
                newTerm.next = current.next;
                current.next = newTerm;
            }
        }
    }

    // Method to add two polynomials
    public Polynomial add(Polynomial rhs) {
        Polynomial result = new Polynomial();
        Literal p1 = this.head;
        Literal p2 = rhs.head;

        while (p1 != null && p2 != null) {
            if (p1.getExponent() == p2.getExponent()) {
                result.insertTerm(p1.getCoefficient() + p2.getCoefficient(), p1.getExponent());
                p1 = p1.next;
                p2 = p2.next;
            } else if (p1.getExponent() > p2.getExponent()) {
                result.insertTerm(p1.getCoefficient(), p1.getExponent());
                p1 = p1.next;
            } else {
                result.insertTerm(p2.getCoefficient(), p2.getExponent());
                p2 = p2.next;
            }
        }

        // Handle remaining terms in either polynomial
        while (p1 != null) {
            result.insertTerm(p1.getCoefficient(), p1.getExponent());
            p1 = p1.next;
        }

        while (p2 != null) {
            result.insertTerm(p2.getCoefficient(), p2.getExponent());
            p2 = p2.next;
        }

        return result;
    }

    // Method to multiply two polynomials
    public Polynomial multiply(Polynomial rhs) {
        Polynomial result = new Polynomial();
        Literal p1 = this.head;

        while (p1 != null) {
            Literal p2 = rhs.head;
            while (p2 != null) {
                result.insertTerm(p1.getCoefficient() * p2.getCoefficient(), p1.getExponent() + p2.getExponent());
                p2 = p2.next;
            }
            p1 = p1.next;
        }

        return result;
    }

    // toString method to display the polynomial in the correct format
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Literal current = head;

        while (current != null) {
            if (current.getCoefficient() != 0) {
                sb.append((current.getCoefficient() > 0 && current != head ? "+" : "") + current.getCoefficient() + "x^" + current.getExponent() + " ");
            }
            current = current.next;
        }

        return sb.toString().trim();
    }
}
