#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if cycle list
 * @list: pointer for check
 * Return: 1 or 0
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
