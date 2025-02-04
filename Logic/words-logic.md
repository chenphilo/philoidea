proposition 命题 命題  
symbol 符号 記号        
term 项 項  
constant 常元 定数（定項）
-   tautology (⊤) 永真式 恒真式  
    contradiction (⊥) 永假式 矛盾式 

variable 变元 変項  
bound variable 束缚变元 束縛変項  
free variable 自由变元 自由変項  
function symbol 函数符号 関数記号  
predicate symbol 谓词符号 述語記号  
atomic formula 原子命题 原子論理式  
logical connective 逻辑联结词 論理結合子
-   negation (¬) 否定 否定  
    conjunction (∧) 合取 連言  
    disjunction (∨) 析取 選言  
    implication (→) 蕴涵 含意  
    biconditional (↔) 双条件 等値  
    exclusive or (⊕) 异或 排他的論理和  
    nand (↑) 非与 否定積  
    nor (↓) 非或 否定和   

technical symbol:
- bracket (()) 括号 括弧  

universal quantifier 全称量词 全称限量子  
existential quantifier 存在量词 存在限量子  
induction hypothesis 归纳假设 帰納仮定
- 例：論理式 $F$ 性質 $P$ を満たすことを証明する：  
    Base Case 基本部分: 原子論理式は $P(PV)$ である  
    Hypothesis 仮定:　もし $P(\phi_1), P(\phi_2)$   
    帰納ステップ Inductive Step: $P(\phi_1\vee\phi_2)$...  
    結論: 論理式 $F$ 性質 $P$ を満たす

formula 公式 論理式  
  - Complexity 复杂度 複雑性:   
    $d(\alpha) := 0$  
    $d(\neg\varphi) := d(\varphi) + 1$   
    $d(\varphi\rightarrow\psi) := d(\varphi) + d(\psi)+ 1$   
    $d(\forall\varphi) := d(\varphi) + 1$ 

证明长度
  - <details>
    ![alt text](prooflength.png)
    </details>

logic 逻辑 論理
  - a reason: $(\Gamma, \varphi)\in {\mathcal{P}(\mathcal{L})}\times\mathcal{L}$
  - logic (用了证明论逻辑的常用符号，但这里代表一般性逻辑):  $\mathbf{L}=(\mathcal{L}, \vdash)$, where $\vdash \subseteq \mathcal{P}(\mathcal{L})\times\mathcal{L}$
  - 性質:  
      Reflexive 自反性 反射的 (はんしゃてき): $\varphi\vdash\varphi$  
      Transitive 传递性 推移的 (すいいてき): If $\Gamma\vdash\Sigma$ and $\Sigma\vdash\varphi$, then $\Gamma\vdash\varphi$  
      Monotonicity 单调性 単調性 (たんちょうせい): If $\Gamma\vdash\varphi$ and $\Gamma\subseteq\Sigma$, then $\Sigma\vdash\varphi$  
      Compact 紧致的 コンパクト: If $\Gamma\vdash\varphi$, then exist finite set $\Phi\vdash\varphi$  
      Formal/structural 形式的 形式的: If $\Sigma\vdash\varphi$, then $\Sigma^\sigma\vdash\varphi\sigma$  
      Extension 扩张 拡張: $\mathbf{L'}$ is extended logic of $\mathbf{L}$ iff $\vdash \subseteq \vdash'$  
  - 意味論理論: 
    - 表达力与不变性
    - 可定义性
    - 有穷模型性  
  - 証明論理論:
    - 性质优良的证明系统
    - 考不同逻辑之间的关系
    - 証明方法: induction on the length of the proof.
      - $(\varphi_1, \varphi_2... \varphi_n)$
  - 証明論理論と意味論理論の関係:
    - 規則関係
      - 可允规则 $R$ : for any $(\Sigma,\varphi)\in R: \vdash\Sigma \Rightarrow \vdash\varphi$  
      - 导出规则 $R$ : for any $(\Sigma,\varphi)\in R: \Sigma\vdash\varphi$  
      - 有效规则 $R$ : for any $(\Sigma,\varphi)\in R: \vDash\Sigma \Rightarrow \vDash\varphi$
      - 保真规则 $R$ : for any $(\Sigma,\varphi)\in R: \Sigma\vDash\varphi$    
    - 健全性: $\vdash\varphi\Rightarrow\vDash\varphi$
      - 強健全性: $\vDash\subset\vdash$
      - <details>
        ![Proof Diagram](pic/soundness.png)
        </details>

    - 完全性: $\vDash\varphi\Rightarrow\vdash\varphi$
      - 強完全性: $\vdash\subset\vDash$
      - 証明   


-------
proposition logic 命题逻辑 命題論理
- 意味論体系（モデル論理） $\mathbf{PC} = (V, \vDash)$
  - Domain 论域 論域
  - Assignment 赋值 割当
  - Truth conditions 真值条件 真理条件
    - Truth table 真值表 真理値表
- 公理体系（証明論論理）
  - 公理    
    - PC1: $\quad p \to (q \to p)$   
    - PC2: $\quad (p \to (q \to r)) \to ((p \to q) \to (p \to r))$  
    - PC3: $\quad (\neg p \to q) \to ((\neg p \to \neg q) \to p)$  
  - rule:   
    - US: $\frac{\phi}{\psi^\sigma}$
    - MP: $\frac{\phi, \phi\rightarrow\psi}{\psi}$
- 自然演繹体系（証明論論理）
    - Gerhard Gentzen 根岑 1934-1935  
    - Elimination Rule 消除规则 除去規則

        $\frac{
        A \quad \neg A
        }{
        \bot
        }
        \neg E, 
        \frac{
        A \land B
        }{
        A
        }
        \land E_1
        \quad
        \frac{
        A \land B
        }{
        B
        }
        \land E_2, 
        \frac{
        A \lor B \quad
        \begin{array}{c}
            [A]^1 \\ 
            \vdots \\
            C
        \end{array}
        \quad
        \begin{array}{c}
            [B]^2 \\ 
            \vdots \\
            C
        \end{array}
        }{
        C
        }
        \lor E^{1,2}, 
        \frac{
        A \rightarrow B \quad A
        }{
        B
        }
        \rightarrow E$
    - Introduction Rule 引入规则 導入規則  
  
        $\frac{
        \begin{array}{c}
            [\neg A]^1 \\ 
            \vdots \\
            \bot
        \end{array}
        }{
        A
        }
        \neg I^1, 
        \frac{
        A \quad B
        }{
        A \land B
        }
        \land I, 
        \frac{
        A
        }{
        A \lor B
        }
        \lor I_1
        \quad
        \frac{
        B
        }{
        A \lor B
        }
        \lor I_2, 
        \frac{
        \begin{array}{c}
            [A]^1 \\ 
            \vdots \\
            B
        \end{array}
        }{
        A \rightarrow B
        }
        \rightarrow I^1$  
    - Reductio ad Absurdum 归谬法 反证法

        $\frac{
        \begin{array}{c}
            [\neg A]^1 \\ 
            \vdots \\
            \bot
        \end{array}
        }{
        A
        }
        RA^1$  

first-order logic 一阶逻辑 一階論理
- 公理体系
  - 公理
    - 命題論理公理PC1, PC2, PC3  
    - UD: $\forall x(\phi\rightarrow\psi)\rightarrow (\forall x\phi\rightarrow\forall x\psi)$   
    - UI: $\forall x\phi\rightarrow\phi[t/x]$  
    - VG: $\phi\rightarrow\forall x\phi, x\notin Fv(\phi)$  
  - rule:   
    - UG: $\frac{\phi}{\forall x \phi}$
    - MP: $\frac{\phi, \phi\rightarrow\psi}{\psi}$
- 自然演繹
  - Elimination Rule 消除规则 除去規則
    - 同命題规则, 
        $\frac{
        \forall x P(x)
        }{
        P(a)
        }
        \forall E, 
        \frac{
        \exists x P(x) \quad
        \begin{array}{c}
            [P(a)]^1 \\ 
            \vdots \\
            C
        \end{array}
        }{
        C
        }
        \exists E^1$
  - Introduction Rule 引入规则 導入規則  
    - 同命題规则, 
        $\frac{
        \begin{array}{c}
            P(x) \\ 
            for any x
        \end{array}
        }{
        \forall x P(x)
        }
        \forall I, 
        \frac{
        P(a)
        }{
        \exists x P(x)
        }
        \exists I$

second-order logic 二阶逻辑 二階論理  
axiom 公理 公理  
theorem 定理 定理  
proof 证明 証明  
model 模型 モデル  
interpretation 解释 解釈  
validity 有效性 妥当性  
satisfiability 可满足性 充足性  
provability 可证性 証明可能性    
soundness 可靠性 健全性 
- 一階論理健全性の証明ツール：  
  - 公理は全部妥当である：  
    - 命題公理パターンは全部妥当である
    - 述語公理パターンは全部妥当である
  - MPとUGが $\vDash$ においても成立する

completeness 完备性 完全性
- canonical model 典范模型 カノニカルモデル

Löwenheim-Skolem 定理   
consistency 一致性 無矛盾性  
decidability 可判定性 決定可能性  
Gödel's incompleteness theorem 哥德尔不完全性定理 ゲーデルの不完全性定理  
recursive function 递归函数 再帰関数  
Turing machine 图灵机 チューリング機械  
lambda calculus λ演算 ラムダ計算  
type theory 类型论 型理論  
propositional logic 命题逻辑 命題論理  
predicate logic 谓词逻辑 述語論理  
modal logic 模态逻辑 様相論理  
intuitionistic logic 直觉主义逻辑 直観主義論理  
fuzzy logic 模糊逻辑 ファジー論理  
set theory 集合论 集合論  
formal system 形式系统 形式体系  
deductive system 演绎系统 演繹体系  
sequent calculus 序列演算 シーケント計算  
natural deduction 自然演绎 自然演繹  
structure 结构 構造
Symmetric 对称性 対称的 (たいしょうてき)  
Antisymmetric 反对称性 反対称的 (はんたいしょうてき)  
Euclidean 欧几里得性 ユークリッド的  
Equivalence relation 等价关系 同値関係 (どうちかんけい)