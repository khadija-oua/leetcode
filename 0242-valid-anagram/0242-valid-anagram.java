class Solution {
    public boolean isAnagram(String s, String t) {
    if(s.length() != t.length()){
        return false;
    }
    HashMap<Character,Integer> T = new HashMap<Character, Integer>();
    HashMap<Character,Integer> S = new HashMap<Character, Integer>();
    for (char c : t.toCharArray()){
        if(T.containsKey(c)){
            T.put(c,T.get(c)+1);
        }
        else{
            T.put(c,1);
        };
    };
     for (char c : s.toCharArray()){
        if(S.containsKey(c)){
            S.put(c,S.get(c)+1);
        }
        else{
            S.put(c,1);

        };
    };
return S.equals(T);



    }
}