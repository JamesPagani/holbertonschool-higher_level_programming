#include "lists.h"
/**
 * list_size - Gets the size of the linked list
 * @head: Head node of the linked list
 * Return: Size of the linked list
 */

int list_size(listint_t *head)
{
	int count = 0;
	listint_t *node = head;

	while (node != NULL)
	{
		count++;
		node = node->next;
	}
	return (count);
}

/**
 * fill_arrays - Fills the dynamic arrays used by is_palindrome
 * @head: Head node of the linked list
 * @arr_a: First half of the linked list
 * @arr_b: Reversed second half of the linked list
 * Return: Nothing
 */

void fill_arrays(listint_t *head, int **arr_a, int **arr_b, int size)
{
	int i;
	listint_t *node = head;

	for (i = 0; i < size / 2; i++)
	{
		(*arr_a)[i] = node->n;
		node = node->next;
	}
	if (size % 2 != 0)
		node = node->next;
	for (i--; i >= 0; i--)
	{
		(*arr_b)[i] = node->n;
		node = node->next;
	}
}

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: Head node of the linked list
 * Return: 1 if the list is a palindrome, 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	int length = list_size(*head);
	int *arr_a, *arr_b;
	int i;

	if (head == NULL || *head == NULL)
		return (1);
	arr_a = malloc((length / 2) * sizeof(int));
	if (arr_a == NULL)
		return (0);
	arr_b = malloc((length / 2) * sizeof(int));
	if (arr_b == NULL)
	{
		free(arr_b);
		return (0);
	}
	fill_arrays(*head, &arr_a, &arr_b, length);
	for (i = 0; i < length / 2; i++)
	{
		if (arr_a[i] != arr_b[i])
		{
			free(arr_a);
			free(arr_b);
			return (0);
		}
	}
	free(arr_a);
	free(arr_b);
	return (1);
}
