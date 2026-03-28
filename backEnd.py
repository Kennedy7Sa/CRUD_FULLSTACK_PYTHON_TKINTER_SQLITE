import sqlite3


def conexao():
    return sqlite3.connect('bd_tarefas.db')


class Tarefa:
    def __init__(self, dados):
        self.id = dados.get('id')
        self.nome = dados.get('nome')
        self.status = dados.get('status')

    def salvar(self):
        banco = conexao()
        cursor = banco.cursor()

        try:
            if self.id:
                cursor.execute(
                    'UPDATE TAREFAS SET nome=?, status=? WHERE id=?',
                    (self.nome, self.status, self.id)
                )
                print(f'Tarefa {self.id} atualizada com sucesso')
            else:
                cursor.execute(
                    'INSERT INTO TAREFAS (nome, status) VALUES (?, ?)',
                    (self.nome, self.status)
                )
                print(f'Tarefa {self.nome} criada com sucesso')

            banco.commit()

        except sqlite3.Error as erro:
            print(f'Erro: {erro}')

        finally:
            banco.close()

    def excluir(self):
        banco = conexao()
        cursor = banco.cursor()

        try:
            cursor.execute('DELETE FROM TAREFAS WHERE id=?', (self.id,))
            banco.commit()

            if cursor.rowcount > 0:
                print(f'Tarefa {self.id} excluída')
            else:
                print('Tarefa não encontrada')

        except sqlite3.Error as erro:
            print(f'Erro: {erro}')

        finally:
            banco.close()

    @staticmethod
    def listar():
        banco = conexao()
        cursor = banco.cursor()

        dados = cursor.execute('SELECT * FROM TAREFAS').fetchall()

        banco.close()

        return [
            {'id': t[0], 'nome': t[1], 'status': t[2]}
            for t in dados
        ]