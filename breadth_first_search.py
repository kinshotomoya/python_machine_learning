# 幅優先探索アルゴリズム
# ターゲットまでの最短経路を見つけるアルゴリズム
# これは、各辺に重みの違いが存在しない場合に有効

from collections import deque

graph = {}
graph['you'] = ['tomoya', 'nana', 'ikuya']
graph['tomoya'] = ['mimi']
graph['nana'] = ['mimi']
graph['ikuya'] = ['papa', 'mama']
graph['mimi'] = []
graph['papa'] = []
graph['mama'] = []

def search_target(name):
    search_queue = deque()
    edge = 1
    search_queue += [{n: edge} for n in graph[name]]
    # print(search_queue)
    # 探索済みのノードを格納する
    searched_person = []
    # 辺の合計の長さ
    while search_queue:
        search_person = search_queue.popleft()
        if not search_person in searched_person:
            # 最初の文字がmで始まる人を探索
            if list(search_person.keys())[0][0] == 'm':
                print(search_person)
                return True
            # 辺を追加
            # 隣接ノードの辺の長さは、親元ノードの辺の長さ + 1になる
            edge = list(search_person.values())[0] + 1
            search_queue += [{n: edge} for n in graph[list(search_person.keys())[0]]]
            searched_person.append(search_person)


search_target('you')
