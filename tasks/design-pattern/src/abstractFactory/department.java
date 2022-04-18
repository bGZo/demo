package abstractFactory;

/* File Name: user
 * Author: @bGZo
 * Created Time: 3/31/2022 22:20
 * License: MIT
 * Description:
 */
public class user {
    private int _id;
    private String _name;

    public int get_id(){
        return _id;
    }
    public void set_id(int _id) {
        this._id = _id;
    }

    public String get_name(){
        return _name;
    }
    public void set_name(String _name) {
        this._name = _name;
    }
}
