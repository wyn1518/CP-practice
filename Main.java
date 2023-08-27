import java.util.*;
import java.io.*;

public class Main{
	public static void main(String[] args) throws IOException{
    	IO io = new IO();
        
        Trie trie = new Trie();
        
        char[] word = io.next().toCharArray();
        int n = io.nextInt();
        for(int i = 0;i < n;i++){
            trie.insert(io.next().toCharArray());
        }   
        io.println(trie.search(word,word.length));


		io.close();
	}
    static class Node{
        public Map<Character,Node> character;
        public boolean end;
        public Node(){
            this.character = new TreeMap<>();
            this.end = false;
        }
    }
    static class Trie{
        public Node root;
        public Trie(){
            this.root = new Node();
        }

        public void insert(char[] word){
            Node node = this.root;
            for(char c:word){
                if(!node.character.containsKey(c)){
                    node.character.put(c,new Node());
                }
                node = node.character.get(c);
            }
            node.end = true;
        }
        public int search(char[] word,int n){
            
            int[] ans = new int[n+1];
            ans[n] = 1;
            for(int i = n-1;i >= 0;i--){
                Node node = this.root;
                for(int j = i;j < n;j++){
                    if(!node.character.containsKey(word[j]))
                        break;

                    node = node.character.get(word[j]);
                    if(node.end){
                        int mod = 1000000007;
                        ans[i] = (ans[i]%mod + ans[j+1]%mod)%mod;
                    }
                }
            }

            return ans[0];
        }
    }
    static class IO extends PrintWriter {

		private BufferedReader r;

		private StringTokenizer st;

		// standard input


		public IO() { this(System.in, System.out); }
		public IO(InputStream i, OutputStream o) {

			super(o);

			r = new BufferedReader(new InputStreamReader(i));

		}

		public IO(String problemName) throws IOException {

			super(problemName + ".out");

			r = new BufferedReader(new FileReader(problemName + ".in"));

		}
		
		public String next() {

			try {

				while (st == null || !st.hasMoreTokens())

					st = new StringTokenizer(r.readLine());

				return st.nextToken();

			} catch (Exception e) { }

			return null;

		}
		public char nextChar(){return next().charAt(0);}
		public int nextInt() { return Integer.parseInt(next()); }

		public double nextDouble() { return Double.parseDouble(next()); }

		public long nextLong() { return Long.parseLong(next()); }

	}
    
}







