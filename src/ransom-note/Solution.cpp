// https://leetcode.com/problems/ransom-note

class Solution{
  public:
    bool canConstruct(std::string ransomNote, std::string magazine){
      std::vector<int> v {{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}} ;
      for(auto& l:magazine){
        v[int(l)-int('a')]+=1;
      }   
      for(auto& l:ransomNote){
        --v[int(l)-int('a')]<0;
      }
      for(auto& i:v){
        if(i < 0)return false;
      }
      return true;
    }   
};


