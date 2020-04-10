package CPP.Absyn; // Java Package generated by the BNF Converter.

public class SBlock  extends Stm {
  public final ListStm liststm_;
  public SBlock(ListStm p1) { liststm_ = p1; }

  public <R,A> R accept(CPP.Absyn.Stm.Visitor<R,A> v, A arg) { return v.visit(this, arg); }

  public boolean equals(Object o) {
    if (this == o) return true;
    if (o instanceof CPP.Absyn.SBlock) {
      CPP.Absyn.SBlock x = (CPP.Absyn.SBlock)o;
      return this.liststm_.equals(x.liststm_);
    }
    return false;
  }

  public int hashCode() {
    return this.liststm_.hashCode();
  }


}
