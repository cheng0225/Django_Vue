<template>
<div class="home">
  <el-row display="margin-top:10px">
  <el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
  <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
  </el-row>
  <!-- <p>{{ things }}</p>
  <p>{{ things.at }}</p>
  <p>{{ things[0].pk }}</p> -->

  <div v-for="thing in things">
    <li>
    {{ thing.pk }}
    {{ thing.fields.name }}
    {{ thing.fields.price }}
    </li>
  </div>



<el-row>
<el-table :data="things" style="width: 100%" border>
  <el-table-column prop="pk" label="编号" min-width="100">
    <template slot-scope="scope">{{ scope.row.pk }}</template>
  </el-table-column>
  <el-table-column prop="name" label="物品" min-width="100">
    <template slot-scope="scope"> {{ scope.row.fields.name }} </template>
  </el-table-column>
  <el-table-column prop="price" label="价格" min-width="100">
    <template slot-scope="scope"> {{ scope.row.fields.price }} </template>
  </el-table-column>
</el-table>
</el-row>

  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '25',
      things: [{"pk": 1, "fields": {"name": "ban", "price": 25}}, {"pk": 2, "fields": {"name": "cheng", "price": 25}}]
    }
  },
  mounted: function () {
    this.showBooks()
  },
  methods: {
    showBooks () {
      this.$http.get('http://127.0.0.1:8000/things/show')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          // var res = JSON.parse(JSON.stringify(response.bodyText))
          console.log(res.list)
          if (res.error_num === 0) {
            this.things = res["list"]
            this.input='查询成功'
          } else {
            this.$message.error('查询书籍失败')
            console.log(res['msg'])
          }
        })
    },
    addBook () {
      this.$http.get('http://127.0.0.1:8000/things/add?name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            this.$message.error('新增书籍失败，请重试')
            console.log(res['msg'])
          }
        })
    }
  }
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
