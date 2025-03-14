// Generated from MiGramatica.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MiGramaticaParser}.
 */
public interface MiGramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MiGramaticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(MiGramaticaParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiGramaticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(MiGramaticaParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterVariable(MiGramaticaParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitVariable(MiGramaticaParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(MiGramaticaParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(MiGramaticaParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(MiGramaticaParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(MiGramaticaParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterParens(MiGramaticaParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitParens(MiGramaticaParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Assign}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterAssign(MiGramaticaParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Assign}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitAssign(MiGramaticaParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Int}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterInt(MiGramaticaParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Int}
	 * labeled alternative in {@link MiGramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitInt(MiGramaticaParser.IntContext ctx);
}