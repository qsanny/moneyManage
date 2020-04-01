<template >
  <div id="app">



<div class="input-group m-3 col-md-6">
  <input type="text" v-model="search" class="form-control" placeholder="Search" aria-label="Recipient's username" aria-describedby="button-addon2">

  <button type="button" class=" ml-5  btn btn-outline-primary" data-toggle="modal" data-target="#exampleModalCenter">
  Add new Budget
</button>
</div>

<!-- Button trigger modal -->


<!-- Modal -->
<div class="modal fade " id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">Add new Budjet</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group row">
            <label for="titre" class="col-sm-2 col-form-label">Titre</label>
            <div class="col-sm-10">
              <input v-model="newBudjet.titre" type="text" class="form-control" id="titre">
              <small>Donner un titre pour reconnaitre le budjet</small>
            </div>

          </div>
          <div class="form-group row">
            <label for="description" class="col-sm-2 col-form-label">Description</label>
            <div class="col-sm-10">
              <input v-model="newBudjet.description" type="text" class="form-control" id="description">
              <small>Expliquer la source de revenue(facultatif mais recommendé)</small>
            </div>
          </div>
          <div class="form-group row">


            <div class="input-group mb">
              <label for="montant" class="col-sm-2 col-form-label">Montant</label>
              <div class="col-sm-8">
                <input v-model="newBudjet.montant" type="number" class="form-control" id="montant">
              </div>
              <div class="input-group-append col-sm-2">
                <span class="input-group-text">FCFA</span>
              </div>
            </div>
          </div>
          <div class="form-group row">
            <div class="input-group mb">
              <label for="restant" class="col-sm-2 col-form-label">Restant</label>
              <div class="col-sm-8">
                <input v-model="newBudjet.restant" type="number" class="form-control" id="restant">
              </div>
              <div class="input-group-append col-sm-2">
                <span class="input-group-text">FCFA</span>
              </div>
            </div>
          </div>

          <div class="form-group row">
            <div class="input-group mb">
              <label for="duree" class="col-sm-2 col-form-label">Durée</label>
              <div class="col-sm-7">
                <input v-model="newBudjet.duree" type="number" class="form-control" id="duree">
              </div>
              <div class="input-group-append col-sm-3">
                <span class="input-group-text">Semaine</span>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="createBudget" >Save changes</button>
      </div>
    </div>
  </div>
</div>

<!-- MODAL CREATE DEPENSE -->

<div class="modal fade " id="exampleModalDepense" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">Add new Depense</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group row">
            <label for="titre" class="col-sm-2 col-form-label">Titre</label>
            <div class="col-sm-10">
              <input v-model="newDepense.titre" type="text" class="form-control" id="titre">
              <small>Donner un titre pour reconnaitre le depense</small>
            </div>

          </div>
          <div class="form-group row">
            <label for="description" class="col-sm-2 col-form-label">Description</label>
            <div class="col-sm-10">
              <input v-model="newDepense.description" type="text" class="form-control" id="description">
              <small>Expliquer la source de revenue(facultatif mais recommendé)</small>
            </div>
          </div>
          <div class="form-group row">
            <div class="input-group mb">
              <label for="montant" class="col-sm-2 col-form-label">Montant</label>
              <div class="col-sm-8">
                <input v-model="newDepense.montant" type="number" class="form-control" id="montant">
              </div>
              <div class="input-group-append col-sm-2">
                <span class="input-group-text">FCFA</span>
              </div>
            </div>
          </div>
          <div class="form-group row">
            <div class="input-group mb">
              <label for="duree" class="col-sm-2 col-form-label">Durée</label>
              <div class="col-sm-7">
                <input v-model="newDepense.date" type="text" class="form-control" id="duree">
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Annuler</button>
        <button type="button" class="btn btn-primary" @click="createDepense" >Ajouter la dépense</button>
      </div>
    </div>
  </div>
</div>

<!-- END MODAT CREATE DEPENSE -->

<div class="modal fade" id="exampleModalDetail" tabindex="-1" role="dialog" aria-labelledby="exampleModalDetail" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">Add new Budjet</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group row">
            <label for="titre" class="col-sm-2 col-form-label">Titre</label>
            <div class="col-sm-10">
              <input v-model="detailBudget.titre" type="text" class="form-control" id="titre">
              <small>Donner un titre pour reconnaitre le budjet</small>
            </div>

          </div>
          <div class="form-group row">
            <label for="description" class="col-sm-2 col-form-label">Description</label>
            <div class="col-sm-10">
              <input v-model="detailBudget.description" type="text" class="form-control" id="description">
              <small>Expliquer la source de revenue(facultatif mais recommendé)</small>
            </div>
          </div>
          <div class="form-group row">


            <div class="input-group mb">
              <label for="montant" class="col-sm-2 col-form-label">Montant</label>
              <div class="col-sm-8">
                <input v-model="detailBudget.montant" type="number" class="form-control" id="montant">
              </div>
              <div class="input-group-append col-sm-2">
                <span class="input-group-text">FCFA</span>
              </div>
            </div>
          </div>
          <div class="form-group row">
            <div class="input-group mb">
              <label for="restant" class="col-sm-2 col-form-label">Restant</label>
              <div class="col-sm-8">
                <input v-model="detailBudget.restant" type="number" class="form-control" id="restant">
              </div>
              <div class="input-group-append col-sm-2">
                <span class="input-group-text">FCFA</span>
              </div>
            </div>
          </div>

          <div class="form-group row">
            <div class="input-group mb">
              <label for="duree" class="col-sm-2 col-form-label">Durée</label>
              <div class="col-sm-7">
                <input v-model="detailBudget.duree" type="number" class="form-control" id="duree">
              </div>
              <div class="input-group-append col-sm-3">
                <span class="input-group-text">Semaine</span>
              </div>
            </div>
          </div>
        </form>
      </div>


      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">Dépense details</h5>
      </div>
      <div class="modal-body">
        <div v-for="depense of detailBudget.depensesbudgetSet" v-bind:key="depense.id" >
          <ul>
            <div>
              <div class="id">{{depense.montant}}</div>
              <div class="titre" > {{depense.titre.slice(0,15)}} </div>
              <div class="montant" > {{depense.montant}} FCFA </div>
              <div class="des" > {{depense.description}} </div>
            </div>
          </ul>
        </div>
      </div>


      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="updateBudget" >Save changes</button>
      </div>
    </div>
  </div>
</div>

  <div v-if="$apollo.queries.budgets.loading">Loading...</div>
    <div class="list">
      <div v-for="node in budgets" v-bind:key="node.id" class="_card" >
        <ul>
          <div class="flex_">
            <div class="id"> {{node.id}} . {{node.createdAt}} </div>
            <div class="d-flex flex-row">
              <button type="button" data-toggle="modal" @click="newDepense.idBudget=node.id" data-target="#exampleModalDepense" class="btn btn-outline-primary btn-sm mr-2">+ Dépense</button>
              <button type="button" data-toggle="modal" @click="budgetDetail(node)" data-target="#exampleModalDetail" class="btn btn-outline-primary rounded btn-sm mr-2">Detail</button>
              <button type="button" @click="deleteBudget(node)" class="btn btn-outline-danger rounded-circle btn-sm delete">X</button>

            </div>
          </div>

          <div class="titre" > {{node.titre.slice(0,15)}} </div>
          <div class="montant" > {{node.restant}} / {{node.montant}} FCFA </div>
          <div class="des" > {{node.description}} </div>
          <!-- <div>
            <ul v-for="depense in node.node.depensesbudgetSet.edges" v-bind:key="depense.id" >
              <li>{{depense.node.titre}}</li>
              <li>{{depense.node.description}}</li>
              <li>{{depense.node.montant}}</li>
              <br>
            </ul>
          </div> -->

          <!-- <ApolloQuery :query="">
            <template slot-scope="{ result: { data, loading } }">
              <div v-if="loading">Loading...</div>
              <ul v-else>
                <li v-for="user of data.users" class="user">
                  {{ user.name }}
                </li>
              </ul>
            </template>
    </ApolloQuery> -->
        </ul>
    </div>
    </div>


  </div>
</template>

<script>

import gql from 'graphql-tag'

export const GET_BUDGET = gql`
     query budget($search: String){
        budget(search:$search){
          id
              titre
              description
              montant
              createdAt
              restant
        }
      }
    `
export const GET_BUDGET_DETAIL = gql`
     query detailBudget($id: ID!){
        detailBudget(id:$id){
              id
              titre
              description
              montant
              createdAt
              restant
              duree
              depensesbudgetSet{
                id
                titre
                montant
                date
                createdAt
                description
              }
        }
    }
  `

export const CREATE_DEPENSE = gql`
     mutation createDepense($titre:String!, $description:String!, $montant:Int!, $date:String!, $idBudget:ID!){
        createDepense(titre:$titre, description:$description, montant:$montant, date:$date, idBudget:$idBudget){
          depense{
            id
            titre
            description
            montant
            createdAt
          }
        }
      }
    `











export default {
  name: 'app',

  data () {
    return {
      search:"",
      msg: 'Hello qad',
      budgets: '',
      todos:[],
      newBudjet:{
        titre:"papa",
        description:'desrition papa',
        montant:2000,
        restant:2000,
        duree:1
      },
      newDepense:{},
      detailBudget:'',
      page: 0,
      showMoreEnabled: true,
    }
  },
   apollo: {
    // Apollo specific options

         budgets:{
           query: GET_BUDGET,
           variables(){
             return {
               search:this.search
             }
           },
           update: data => data.budget,
          //  pollInterval: 5000, // ms

         }
  },

  methods: {
    createBudget(){

      const newBudget = this.newBudjet
      //this.newBudjet = ''
      this.$apollo.mutate({
        mutation: gql`
          mutation($titre:String!, $description:String!,  $montant:Int!, $duree:Int!, $restant:Int!){
            createBudget(titre:$titre, description:$description,  montant:$montant, duree:$duree, restant:$restant)
            {
              budget{
                id
                titre
                description
                montant
                createdAt
              }
            }
          }
        `,
          variables:{
            titre:newBudget.titre,
            description:newBudget.description,
            montant:newBudget.montant,
            duree:newBudget.duree,
            restant:newBudget.restant
          },
          update: (store, {data: {createBudget}}) => {
            console.log(store)
             const data = store.readQuery({ query: GET_BUDGET,
                                            variables:{
                                            search:""}
                                          })
            console.log(data)
            data.budget.push(createBudget.budget)
            store.writeQuery({ query: GET_BUDGET, data })

          },

        //   optimisticResponse: {
        //   __typename: 'Mutation',
        //   createBudget: {
        //     __typename: 'Budget',
        //     id: -1,
        //     titre:newBudget.titre,
        //     description:newBudget.description,
        //     montant:newBudget.montant,
        //     duree:newBudget.duree,
        //     restant:newBudget.restant
        //   },
        // },

      }).then((result) =>{
        console.log(result)
        $('#exampleModalCenter').modal('hide')


      }).catch((error) => {
        console.error(error)
      })
    },
    updateBudget(){

      const newBudget = this.detailBudget
      //this.newBudjet = ''
      this.$apollo.mutate({
        mutation: gql`
          mutation($titre:String!, $description:String!,  $montant:Int!, $duree:Int!, $restant:Int!,  $update:Boolean, $id:ID){
            createBudget(titre:$titre, description:$description,  montant:$montant, duree:$duree, restant:$restant,  update:$update, id:$id)
            {
              budget{
                id
                titre
                description
                montant
                createdAt
              }
            }
          }
        `,
          variables:{
            titre:newBudget.titre,
            description:newBudget.description,
            montant:newBudget.montant,
            duree:newBudget.duree,
            restant:newBudget.restant,
            update:true,
            id:newBudget.id
          },
          update: (store, {data: {createBudget}}) => {
            console.log(store)
             const data = store.readQuery({ query: GET_BUDGET,
                                            variables:{
                                            search:""}
                                          })
            console.log(data)
            data.budget.forEach(budget => {
              if(budget.id == createBudget.budget.id){
                budget = createBudget.budget
              }
            });
            // data.budget.push(createBudget.budget)
            store.writeQuery({ query: GET_BUDGET, data })

          },

        //   optimisticResponse: {
        //   __typename: 'Mutation',
        //   createBudget: {
        //     __typename: 'Budget',
        //     id: -1,
        //     titre:newBudget.titre,
        //     description:newBudget.description,
        //     montant:newBudget.montant,
        //     duree:newBudget.duree,
        //     restant:newBudget.restant
        //   },
        // },

      }).then((result) =>{
        console.log(result)
        $('#exampleModalDetail').modal('hide')


      }).catch((error) => {
        console.error(error)
      })
    },

    deleteBudget(budget){
      console.log(budget)

      const dbudget = budget

      const DELETE_BUDGET = gql`mutation($id:ID!){
        deleteBudget(id: $id){
          budget{
            id
          }
        }
      }
      `
      this.$apollo.mutate({
        mutation: DELETE_BUDGET,
        variables:{
          id:budget.id
        },update: (store, {data: {deleteBudget}}) => {
            console.log(store)
             const data = store.readQuery({ query: GET_BUDGET,
                                            variables:{
                                            search:""}
                                          })
            console.log(data)
            const i = data.budget.indexOf(dbudget)
            data.budget.splice(i,1)
            store.writeQuery({ query: GET_BUDGET, data })

          },

      }).then((result) => {
      }).catch((error) =>{
        console.error(error)
      })
    },

    budgetDetail(node){
      console.log(node)
      this.$apollo.addSmartQuery('detailBudget',{
        query:GET_BUDGET_DETAIL,
        variables:{
          id:node.id
        },
        update: data =>data.detailBudget
      })
    },

    createDepense(){
      this.$apollo.mutate({
        mutation: CREATE_DEPENSE,
        variables:{
          titre:this.newDepense.titre,
          description:this.newDepense.description,
          montant:this.newDepense.montant,
          date:this.newDepense.date,
          idBudget: this.newDepense.idBudget
        },
      }).then((result)=>{
        console.log(result)
        this.detailBudget.depensesbudgetSet.push(result)

        //stuff after depense creation
      }).catch((error)=>{
        console.error(error)
      })
    },
    deleteDepense(id){
      this.$apollo.mutate({
        mutation: gql`
          mutation deleteDepense($id:ID){
            deleteDepense(id:$id)
          }
        `,
        variables:{
          id:id
        },
      }).then((result)=>{
        console.log(result)
        //stuff after depense deletion
      }).catch((error)=>{
        console.error(error)
      })
    }
  },



}
</script>

<style>
#app{


}
._card{
  width: 33%;


  margin-bottom: 50px
}
  ul{
    border: 2px solid rgba(41, 9, 92, 0.856);
    background-color: rgba(54, 19, 110, 0.801);
    color: white;
    border-radius: 5px;
    margin: 5px;
    margin-bottom: 25px;
    margin-left: 20px;
    padding: 10px;
    border-top-right-radius: 25px;
    height: 300px;
      overflow: hidden;


  }

  .titre{
    text-align: center;
    font-size: 25px;
    font-weight: bold;
  }
  .des{
    color: rgba(240, 248, 255, 0.637)
  }
  .montant{
    color: rgb(235, 238, 53);
    padding: 7px;
    margin: 3px;
    border: 2px solid rgb(253, 255, 136);
    border-radius: 25px;
    text-align: center;
  }
  li{
    list-style-type: none;
  }
  .id{
    font-size: 11px;
  }
  .list{
    display: flex;
    flex-wrap: wrap;
  }
  .flex_{
    display: flex;
    /* position: relative; */
    justify-content: space-between;

  }
  .delete{
    color: red;
    /* position: absolute; */
    right: 0px;

  }

</style>
