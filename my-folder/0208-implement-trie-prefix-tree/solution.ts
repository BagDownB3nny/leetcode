class Node {
    val: string;
    nodes: Node[];
    nodesMap: { [key: string]: Node };
    isEnd: boolean;
    
    constructor(val: string, nodes: Node[], isEnd: boolean) {
        this.val = val;
        this.nodes = nodes;
        this.nodesMap = {};
        for (const node of nodes) {
            this.nodesMap[node.val] = node;
        }
        this.isEnd = isEnd;
    }

    addNode(node: Node) {
        this.nodes.push(node);
        this.nodesMap[node.val] = node;
    }

    hasChild(c: string): boolean {
        return (!!this.nodesMap[c]);
    }

    getChild(c: string) {
        return this.nodesMap[c];
    }

    markAsWordEnd() {
        this.isEnd = true;
    }
}

class Trie {
    root: Node;
    
    constructor() {
        this.root = new Node("_", [], false);
    }

    insert(word: string): void {
        let currentNode = this.root;
        
        for (let i = 0; i < word.length; i++) {
            const c = word.charAt(i);
            if (currentNode.hasChild(c)) {
                currentNode = currentNode.getChild(c);
            } else {
                const newNode = new Node(c, [], false);
                currentNode.addNode(newNode);
                currentNode = newNode;
            }
        }
        currentNode.markAsWordEnd();
    }

    search(word: string): boolean {
        let currentNode = this.root;
        
        for (let i = 0; i < word.length; i++) {
            const c = word.charAt(i);
            if (currentNode.hasChild(c)) {
                currentNode = currentNode.getChild(c);
            } else {
                return false;
            }
        }
        return currentNode.isEnd;
    }

    startsWith(prefix: string): boolean {
        let currentNode = this.root;
        
        for (let i = 0; i < prefix.length; i++) {
            const c = prefix.charAt(i);
            if (currentNode.hasChild(c)) {
                currentNode = currentNode.getChild(c);
            } else {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
