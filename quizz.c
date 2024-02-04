#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
    char question[256];
    char options[4][64];
    int correct_option;
} Question;

void displayQuestion(Question q) {
    printf("%s\n", q.question);
    for (int i = 0; i < 4; i++) {
        printf("%d. %s\n", i + 1, q.options[i]);
    }
}

int main() {
    srand(time(NULL));

    Question placeholder_questions[3] = {
        {"What is the capital of France?",
         {"Paris", "Berlin", "London", "Madrid"},
         1},
        {"Which planet is known as the Red Planet?",
         {"Venus", "Mars", "Jupiter", "Saturn"},
         2},
        {"Who wrote 'Romeo and Juliet'?",
         {"Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"},
         2}
    };

    for (int i = 0; i < 3; i++) {
        Question current_question = placeholder_questions[i];
        displayQuestion(current_question);

        int user_answer;
        printf("Enter your answer (1-4): ");
        scanf("%d", &user_answer);

        printf("{ \"question\": \"%s\", \"options\": [\"%s\", \"%s\", \"%s\", \"%s\"], \"correct_option\": %d }\n",
               current_question.question,
               current_question.options[0],
               current_question.options[1],
               current_question.options[2],
               current_question.options[3],
               current_question.correct_option);
        
        printf("Expected Answer: %d\n", current_question.correct_option);
    }

    return 0;
}
