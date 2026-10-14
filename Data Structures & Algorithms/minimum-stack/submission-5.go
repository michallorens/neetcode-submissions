type MinStack struct {
	Stack []int
	MinStack []int
}

func Constructor() MinStack {
	return MinStack{Stack: make([]int, 0)}
}

func (this *MinStack) Push(val int) {
	this.Stack = append(this.Stack, val)
	if len(this.MinStack) > 0 {
		this.MinStack = append(this.MinStack, min(val, this.MinStack[len(this.MinStack)-1]))
	} else {
		this.MinStack = append(this.MinStack, val)
	}
}

func (this *MinStack) Pop() {
	this.Stack = this.Stack[:len(this.Stack)-1]
	this.MinStack = this.MinStack[:len(this.MinStack)-1]
}

func (this *MinStack) Top() int {
	return this.Stack[len(this.Stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.MinStack[len(this.MinStack)-1]
}
