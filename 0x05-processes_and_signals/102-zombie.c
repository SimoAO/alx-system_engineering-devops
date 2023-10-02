#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>

/**
 * infinite_while - A function for an infinite loop
 * Return: None
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - A C program that creates 5 zombie processes.
 * Return: None
 */

int main(void)
{
	int i = 0;
	pid_t cp = fork();

	for (; i < 5; i++)
	{
		if (cp > 0)
			printf("Zombie process created, PID: %d\n", cp);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
