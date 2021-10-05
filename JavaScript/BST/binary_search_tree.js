class Binary_Search_Tree_Node {
    constructor(data){
        this.data = data
        this.left = null
        this.right = null
    }
}


class Binary_Search_Tree{
    constructor(){
        this.root = null
    }
    insert(BST_Node){
        if(this.root == null){
            this.root = BST_Node
            return this.root
        }
        else{
            let runner = this.root
            while(runner!=null){
                if(BST_Node.data < runner.data ){
                    if(runner.left == null){
                        runner.left = BST_Node
                        return this.root
                    }
                    else{
                        runner = runner.left
                    }
                }
                else{
                    if (runner.right = null){
                        runner.right = BST_Node
                        return this.root
                    }
                    else{
                        runner = runner.right
                    }
                }
            }
        }
    }
    contains(data){
        let runner = this.root
            while(runner!=null){
                if(runner.data == data){
                    return true
                }
                else if(data<runner.data){
                    runner = runner.left
                }
                else{
                    runner = runner.right
                }
            }
        return false
    }


}
