#include "lists.h"
/**
 * check_cycle - Checks if the linked list has a cycle
 * @list: Pointer to a linked list
 * Return: 0 if there is not a cycle in the linked list, 1 if a cycle was found
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	while (turtle && hare)
	{
		turtle = turtle->next;
		hare = hare->next;
		if (hare == NULL)
			return (0);
		hare = hare->next;

		if (turtle == hare)
		{
			hare = list;
			while (turtle && hare)
			{
				if (turtle == hare)
					return (1);
				hare = hare->next;
				turtle = turtle->next;
			}
		}
	}
	return (0);
}
