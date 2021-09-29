package stone;
import stone.ast.ASTree;

public class StoneException {
    public StoneException(String m){ super(m); }
    public StoneException(String m, ASTree t){
        super(m + ' ' + t.location());
    }
}
