# dog

３Dプリンタでつくる犬型ロボットを動かすためのプログラムと、3Dプリンタ用のモデルです。
今のところ前進するプログラムのみ作成してます。
→元記事:３Ｄプリンタで作るいいかげんロボティクス（第２回）：犬猫ロボット　（https://qiita.com/wilted_cabbage/items/bf660707192d92eb989b）

main.py→メイン関数。RoboDog.pyで作ったモーションを再生します。

RoboDog.py→サーボの角度を組み合わせて、ロボの動きを作ります。

servo_set.py→サーボ角度を90度に設定します。

ServoMovingList.py→RoboDog.pyで設定したモーションの情報をもとに、サーボの角度を設定します。
