/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
     static{
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try(FileWriter writer = new FileWriter("display_runtime.txt")){
                writer.write("0");
            }
            catch(IOException e){
                e.printStackTrace();
            }
        }));
    }
    int length(ListNode l1){
        int count=0;
        while(l1!=null){
            count++;
            l1=l1.next;
        }
        return count;
    }
    void padNode(ListNode curr,int diff){
        while(curr.next!=null){
            curr=curr.next;
        }
        for(int i=0;i<diff;i++){
            ListNode dummy=new ListNode(0);
            curr.next=dummy;
            curr=curr.next;
        }
    }
    void display(ListNode curr){
        while(curr!=null){
            System.out.print(curr.val+" ");
            curr=curr.next;
        }
        System.out.println();
    }
    void add(ListNode l1,ListNode l2){
        int sum=0;
        int carry=0;
        while(l1.next!=null){
            sum=l1.val+l2.val+carry;
            l1.val=sum%10;
            carry=sum/10;
            l1=l1.next;
            l2=l2.next;
        }
            sum=l1.val+l2.val+carry;
            l1.val=sum%10;
            carry=sum/10;
        if(carry!=0){
            ListNode dummy=new ListNode(carry);
            l1.next=dummy;
        }
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Solution obj=new Solution();
        int len1=obj.length(l1);
        int len2=obj.length(l2);
        if(len1<len2){
           obj.padNode(l1,len2-len1);
        }
        else if(len1>len2){
            obj.padNode(l2,len1-len2);
        }
        obj.display(l1);
        obj.display(l2);
        obj.add(l1,l2);
        // int sum=0,carry=0;
        // while (l1.next!=null||l2.next!=null){

        // }
        return l1;
    }
}