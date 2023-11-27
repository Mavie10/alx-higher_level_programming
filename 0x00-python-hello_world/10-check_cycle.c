#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return (1);
    }

    return (0);
}
