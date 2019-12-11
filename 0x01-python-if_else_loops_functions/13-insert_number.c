#include "lists.h"
/**
 * insert_node - Inserts a new node in a sorted singly linked list
 * @head: Head of the list
 * @number: Content of the node
 * Return: The address of the new node; NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *prev = NULL, *curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (head == NULL)
	{
		*head = new;
		return (new);
	}
	if (new->n < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (curr)
	{
		prev = curr;
		curr = curr->next;
		if (curr == NULL || new->n < curr->n)
		{
			prev->next = new;
			new->next = curr;
			return (new);
		}
	}
	return (NULL);
}
