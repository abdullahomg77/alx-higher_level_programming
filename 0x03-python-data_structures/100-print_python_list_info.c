#include <Python.h>

/**
 * print_python_list_info - Prin Python lists
 * @p: Pthon Object list.
*/

void print_python_list_info(PyObject *p)
{
	int s, a, i;
	PyObject *obj;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

