#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct Account {
	int accountNumber;
    char name[50];
    float balance;
};


void createAccount();
void depositMoney();
void withdrawMoney();
void checkBalance();

const char* FILE_NAME = "bank_data.dat";

int main() {
    int choice;

    while (1) {
        printf("\n=== BANK MANAGEMENT SYSTEM ===");
        printf("\n1. Create New Account");
        printf("\n2. Deposit Money");
        printf("\n3. Withdraw Money");
        printf("\n4. Check Balance");
        printf("\n5. Exit");
        printf("\nEnter your choice (1-5): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: createAccount(); break;
            case 2: depositMoney(); break;
            case 3: withdrawMoney(); break;
            case 4: checkBalance(); break;
            case 5: 
                printf("\nThank you for using our banking system!\n");
                exit(0);
            default: 
                printf("\nInvalid choice! Please try again.\n");
        }
    }
    return 0;
}

void createAccount() {
    FILE *file = fopen(FILE_NAME, "ab");
    if (file == NULL) {
        printf("\nError opening file!");
        return;
    }

    struct Account acc;
    printf("\nEnter Account Number: ");
    scanf("%d", &acc.accountNumber);
    printf("Enter Name: ");
    scanf(" %[^\n]s", acc.name); 
    printf("Enter Initial Deposit Amount: ");
    scanf("%f", &acc.balance);

    fwrite(&acc, sizeof(struct Account), 1, file);
    fclose(file);

    printf("\nAccount created successfully!\n");
}

void depositMoney() {
    FILE *file = fopen(FILE_NAME, "rb+");
    if (file == NULL) {
        printf("\nNo accounts found!");
        return;
    }

    int accNo, found = 0;
    float amount;
    struct Account acc;

    printf("\nEnter Account Number: ");
    scanf("%d", &accNo);

    while (fread(&acc, sizeof(struct Account), 1, file)) {
        if (acc.accountNumber == accNo) {
            printf("Current Balance: %.2f", acc.balance);
            printf("\nEnter Deposit Amount: ");
            scanf("%f", &amount);

            acc.balance += amount;
            
            fseek(file, -sizeof(struct Account), SEEK_CUR);
            fwrite(&acc, sizeof(struct Account), 1, file);
            
            printf("\nAmount deposited successfully! New Balance: %.2f\n", acc.balance);
            found = 1;
            break;
        }
    }

    if (!found) printf("\nAccount not found!\n");
    fclose(file);
}

void withdrawMoney() {
    FILE *file = fopen(FILE_NAME, "rb+");
    if (file == NULL) {
        printf("\nNo accounts found!");
        return;
    }

    int accNo, found = 0;
    float amount;
    struct Account acc;

    printf("\nEnter Account Number: ");
    scanf("%d", &accNo);

    while (fread(&acc, sizeof(struct Account), 1, file)) {
        if (acc.accountNumber == accNo) {
            printf("Current Balance: %.2f", acc.balance);
            printf("\nEnter Amount to Withdraw: ");
            scanf("%f", &amount);

            if (amount > acc.balance) {
                printf("\nInsufficient balance!\n");
            } else {
                acc.balance -= amount;
                fseek(file, -sizeof(struct Account), SEEK_CUR);
                fwrite(&acc, sizeof(struct Account), 1, file);
                printf("\nAmount withdrawn successfully! New Balance: %.2f\n", acc.balance);
            }
            found = 1;
            break;
        }
    }

    if (!found) printf("\nAccount not found!\n");
    fclose(file);
}


void checkBalance() {
    FILE *file = fopen(FILE_NAME, "rb");
    if (file == NULL) {
        printf("\nNo accounts found!");
        return;
    }

    int accNo, found = 0;
    struct Account acc;

    printf("\nEnter Account Number: ");
    scanf("%d", &accNo);

    while (fread(&acc, sizeof(struct Account), 1, file)) {
        if (acc.accountNumber == accNo) {
            printf("\n=== Account Details ===");
            printf("\nAccount Number: %d", acc.accountNumber);
            printf("\nAccount Holder: %s", acc.name);
            printf("\nCurrent Balance: %.2f\n", acc.balance);
            found = 1;
            break;
        }
    }

    if (!found) printf("\nAccount not found!\n");
    fclose(file);
}
