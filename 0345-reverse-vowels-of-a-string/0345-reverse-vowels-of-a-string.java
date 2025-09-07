class Solution {
    public String reverseVowels(String s) {
         String[] w = s.split("");
	        List<String> list = new ArrayList<>();
	        for(int i=0;i<w.length;i++) {
	        	if(w[i].toLowerCase().equals("a") || w[i].toLowerCase().equals("e") ||w[i].toLowerCase().equals("i") ||w[i].toLowerCase().equals("o") ||w[i].toLowerCase().equals("u")) {
	        		list.add(w[i]);
	        		}
	        }
	        int n = list.size()-1;
	        for(int i=0;i<w.length;i++) {
	        	if(w[i].toLowerCase().equals("a") || w[i].toLowerCase().equals("e") ||w[i].toLowerCase().equals("i") ||w[i].toLowerCase().equals("o") ||w[i].toLowerCase().equals("u")) {
	        		w[i]=list.get(n);
	        		n--;
	        		}
	        }
	      String res = String.join("", w);
	      return res;  
	    }
}