/*Implement C++ program for expression conversion as infix to postfix and its evaluation
using stack based on given conditions:
1. Operands and operator, both must be single character.
2. Input Postfix expression must be in a desired format.
3. Only '+', '-', '*' and '/ ' operators are expected.*/

#include<iostream>
#include<cstring>
#include<stack>
using namespace std;

// higher weight given to operators with higher precedence
int getWeight(char ch) {
	switch (ch) {
	case '/':
	case '*': return 2;
	case '+':
	case '-': return 1;
	default : return 0;
	}
}

// convert infix expression to postfix using a stack
void infix2postfix(char infix[], char postfix[], int size) {
	stack<char> s;
	int weight;
	int i = 0;
	int k = 0;
	char ch;
	// iterate over the infix expression
	while (i < size) {
		ch = infix[i];
		if (ch == '(') {
			// simply push the opening parenthesis
			s.push(ch);
			i++;
			continue;
		}
		if (ch == ')') 
        {
			while (!s.empty() && s.top() != '(')
            {
				postfix[k++] = s.top();
				s.pop();
			}
			// pop off the opening parenthesis also
			if (!s.empty())
            {
				s.pop();
			}
			i++;
			continue;
		}
		weight = getWeight(ch);
		if (weight == 0)
        {
			// we saw an operand
			// simply append it to postfix expression
			postfix[k++] = ch;
		}
		else
        {
			// we saw an operator
			if (s.empty())
            {
				// simply push the operator onto stack if
				// stack is empty
				s.push(ch);
			}
			else
            {
				/*pop of all the operators from the stack and append it to the postfix expression till we
                see an operator with a lower precedence that the current operator*/
				while (!s.empty() && s.top() != '(' &&weight <= getWeight(s.top()))
                    {
					postfix[k++] = s.top();
					s.pop();
				    }
				// push the current operator onto stack
				s.push(ch);
			}
		}
		i++;
	}
	while (!s.empty()) {
		postfix[k++] = s.top();
		s.pop();
	}
	postfix[k] = 0; // null terminate the postfix expression
}

int main()
{
	char infix[100];//"A*(B+C)/D";
	cout<<"\nEnter Infix Operation : ";
	cin>>infix;
	int size = strlen(infix);
	char postfix[size];
	infix2postfix(infix,postfix,size);
	cout<<"\nInfix Expression : "<<infix;
	cout<<"\nPostfix Expression : "<<postfix;
	cout<<endl;
	return 0;
}